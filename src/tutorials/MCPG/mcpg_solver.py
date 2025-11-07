"""
Copyright (c) 2024 Cheng Chen, Ruitao Chen, Tianyou Li, Zaiwen Wen
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that
the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
   following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
   and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import torch

# 导入我们新增的 TransformerModel 和原始的 simple 模型
from src.model import simple, TransformerModel
from src.sampling import sampler_select, sample_initializer


def mcpg_solver(nvar, config, data, verbose=False):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    sampler = sampler_select(config["problem_type"])

    change_times = int(nvar/10)  # transition times for metropolis sampling

    # ================= 动态模型选择 (Dynamic Model Selection) =================
    # 从配置文件读取要使用的模型类型，如果未指定，则默认为 'simple'
    model_type = config.get("model_type", "simple") 
    
    net = None
    if model_type == "transformer":
        print("===== Using Transformer Model =====")
        # 从配置中读取Transformer的超参数
        # 如果配置中没有 'transformer_params'，则会报错，这是为了提醒用户必须提供参数
        model_params = config['transformer_params']
        net = TransformerModel(
            nvar=nvar,
            embedding_dim=model_params['embedding_dim'],
            num_heads=model_params['num_heads'],
            num_layers=model_params['num_layers'],
            dim_feedforward=model_params['dim_feedforward']
        )
    else: # 默认为 simple 模型
        print("===== Using Simple Model =====")
        model_type = "simple" # 确保变量被设置
        net = simple(nvar)
        
    net.to(device)
    optimizer = torch.optim.Adam(net.parameters(), lr=config['lr_init'])

    start_samples = None
    # 初始化用于存储最佳结果的变量
    # 这一步是为了确保即使在第一个采样周期就找到好结果，也能被正确记录
    now_max_res = torch.full((config['total_mcmc_num'],), float('-inf'), device=device)
    now_max_info = torch.zeros(nvar, config['total_mcmc_num'], device=device)

    for epoch in range(config['max_epoch_num']):

        if epoch % config['reset_epoch_num'] == 0:
            net.reset_parameters()
            regular = config['regular_init']

        net.train()

        # ================= 动态模型调用 (Dynamic Model Invocation) =================
        # 根据模型类型，决定调用 forward 时是否传入 data 对象
        if model_type == "transformer":
            # Transformer 模型需要 data 对象来构建注意力掩码
            if epoch <= 0:
                retdict = net(data, regular, None, None, device=device)
            else:
                retdict = net(data, regular, start_samples, value, device=device)
        else: # simple 模型
            if epoch <= 0:
                retdict = net(regular, None, None, device=device)
            else:
                retdict = net(regular, start_samples, value, device=device)

        retdict["loss"][0].backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(), 1)
        optimizer.step()

        # get start samples (获取初始样本)
        if epoch == 0:
            probs = (torch.zeros(nvar)+0.5).to(device)
            tensor_probs = sample_initializer(
                config["problem_type"], probs, config, data=data)
            temp_max, temp_max_info, temp_start_samples, value = sampler(
                data, tensor_probs, probs, config['num_ls'], 0, config['total_mcmc_num'])
            
            # 首次运行时直接更新最佳结果
            now_max_res = temp_max
            now_max_info = temp_max_info
            
            tensor_probs = temp_max_info.clone()
            tensor_probs = tensor_probs.repeat(1, config['repeat_times'])
            start_samples = temp_start_samples.t().to(device)

        # get samples (获取后续样本)
        if epoch % config['sample_epoch_num'] == 0 and epoch > 0:
            probs = retdict["output"][0].detach() # detach()确保不会有梯度流回
            
            # 使用模型生成的概率进行采样和评估
            temp_max, temp_max_info, start_samples_temp, value = sampler(
                data, tensor_probs, probs, config['num_ls'], change_times, config['total_mcmc_num'])
            
            # update now_max (更新历史最佳结果)
            for i0 in range(config['total_mcmc_num']):
                if temp_max[i0] > now_max_res[i0]:
                    now_max_res[i0] = temp_max[i0]
                    now_max_info[:, i0] = temp_max_info[:, i0]

            # update if min is too small (防止某个探索链的结果过差，用最优结果替换它)
            now_max = max(now_max_res).item()
            now_max_index = torch.argmax(now_max_res)
            now_min_index = torch.argmin(now_max_res)
            
            now_max_res[now_min_index] = now_max
            now_max_info[:, now_min_index] = now_max_info[:, now_max_index].clone() # 使用clone避免引用问题
            temp_max_info[:, now_min_index] = now_max_info[:, now_max_index].clone()

            # select best samples (选择本次采样中最好的样本作为下一次MCMC链的起点)
            tensor_probs = temp_max_info.clone()
            tensor_probs = tensor_probs.repeat(1, config['repeat_times'])
            # construct the start point for next iteration (为下一次模型迭代准备好输入样本)
            start_samples = start_samples_temp.t()
            
            if verbose:
                if config["problem_type"] == "maxsat" and len(data.pdata) == 7:
                    res = max(now_max_res).item()
                    if res > data.pdata[5] * data.pdata[6]:
                        res -= data.pdata[5] * data.pdata[6]
                        print("o {:.3f}".format(res))
                elif "obj_type" in config and config["obj_type"] == "neg":
                    print("o {:.3f}".format((-max(now_max_res).item())))
                else:
                    print("o {:.3f}".format((max(now_max_res).item())))
        
        # 释放显存
        del (retdict)

    total_max = now_max_res
    best_sort = torch.argsort(now_max_res, descending=True)
    total_best_info = torch.squeeze(now_max_info[:, best_sort[0]])

    return max(total_max).item(), total_best_info, now_max_res, now_max_info, net