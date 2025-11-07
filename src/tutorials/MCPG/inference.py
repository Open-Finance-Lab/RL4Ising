# --- inference.py ---
import torch
import yaml
import argparse
import time

# 导入你的模型和数据加载器
from src.model import simple, TransformerModel
from dataloader import dataloader_select
# 导入采样器，因为我们需要用模型生成的策略去采样
from src.sampling import sampler_select, sample_initializer

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # 1. 设置命令行参数
    parser = argparse.ArgumentParser(description="Generalization Test for MCPG Models")
    parser.add_argument("config_file", type=str, help="Configuration file used for TRAINING the model.")
    parser.add_argument("saved_model_path", type=str, help="Path to the saved .pth model file.")
    parser.add_argument("test_instance", type=str, help="Path to the NEW, unseen problem instance for testing.")
    args = parser.parse_args()

    # 2. 加载配置文件以获取模型架构信息
    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    # 3. 加载新问题的测试数据
    dataloader = dataloader_select(config["problem_type"])
    test_data, nvar = dataloader(args.test_instance)
    
    # 4. 初始化模型架构 (必须和训练时完全一致)
    model_type = config.get("model_type", "simple")
    net = None
    if model_type == "transformer":
        print("===== Loading Transformer Model for Inference =====")
        model_params = config['transformer_params']
        net = TransformerModel(nvar=nvar, **model_params)
    else:
        print("===== Loading Simple Model for Inference =====")
        net = simple(nvar=nvar)
        
    # 5. 加载已训练好的模型权重
    net.load_state_dict(torch.load(args.saved_model_path, map_location=device))
    net.to(device)
    net.eval() # !!! 切换到评估模式，这会关闭dropout等训练特有的层

    print(f"Model loaded from {args.saved_model_path}")
    print(f"Testing on instance {args.test_instance} with {nvar} variables.")

    # 6. 执行推理，获取策略 (probs)
        # 6) 前向得到初始概率（只做一次，网络不更新）
    with torch.no_grad():
        if model_type == "transformer":
            retdict = net(test_data, device=device)  # start_samples=None
        else:
            retdict = net(device=device)
        probs = retdict["output"][0].detach().float()

    # 数值安全（避免采样器里 Bernoulli 报错）
    probs = torch.nan_to_num(probs, nan=0.5, posinf=1.0, neginf=0.0).clamp_(1e-6, 1-1e-6)

    # 7) 按“训练期同款”的 MCPG 流程跑一轮（但不更新模型参数）
    #    关键：让 sampler 自己做 MCMC 更换分布 + 多次局部搜索
    sampler = sampler_select(config["problem_type"])

    # 这些超参直接复用训练期配置（或给默认值）
    num_ls_inference = int(config.get("num_ls_inference", config.get("num_ls", 12)))
    change_times_inference = int(config.get("change_times_inference", config.get("change_times", 2)))
    total_mcmc_num = int(config.get("total_mcmc_num", 2000))

    # 用模型给的概率初始化一次样本（和训练时一样）
    tensor_probs = sample_initializer(config["problem_type"], probs, config, data=test_data)

    # 让 sampler 跑完整的一轮：MCMC 变化 change_times 次 + 每次跑若干 LS
    # 注意：sampler 内部只会更新“当前分布/样本”，不会触碰神经网络参数
    with torch.no_grad():
        best_score, best_solution, _, _ = sampler(
            test_data,
            tensor_probs,
            probs,                      # 初始分布
            num_ls_inference,
            change_times_inference,
            total_mcmc_num
        )

    final_result = max(best_score).item()
    if "obj_type" in config and config["obj_type"] == "neg":
        print(f"OUTPUT: {-final_result:.2f}")
    else:
        print(f"OUTPUT: {final_result:.2f}")



if __name__ == "__main__":
    main()