# --- model.py ---
"""
Copyright (c) 2024 Cheng Chen, Ruitao Chen, Tianyou Li, Zaiwen Wen
All rights reserved.
... (copyright text remains the same) ...
"""
import torch
import torch.nn as nn
import math
import torch.nn.functional as F


# ==============================================================================
#  原始的 simple 模型 (保持不变)
# ==============================================================================
class simple(torch.nn.Module):
    def __init__(self, output_num):
        super(simple, self).__init__()
        self.lin = torch.nn.Linear(1,  output_num)
        self.sigmoid = torch.nn.Sigmoid()

    def reset_parameters(self):
        self.lin.reset_parameters()

    def forward(self, alpha = 0.1, start_samples=None, value=None, 
                device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
        # 1. 生成概率: "盲"模型，不看问题结构
        x = torch.ones(1).to(device)
        x = self.lin(x)
        x = self.sigmoid(x)

        x = (x-0.5) * 0.6 + 0.5
        probs = x.squeeze()
        
        retdict = {}
        reg = probs * torch.log(probs) + (1-probs) * torch.log(1-probs)
        reg = torch.mean(reg)
        
        # 如果是第一次调用，只返回概率和正则项
        if start_samples is None:
            retdict["output"] = [probs.squeeze(-1), "hist"]
            retdict["reg"] = [reg, "sequence"]
            retdict["loss"] = [alpha * reg, "sequence"]
            return retdict

        # 2. 计算损失: 使用与求解器交互的反馈
        res_samples = value.t().detach()

        start_samples_idx = start_samples * \
            probs + (1 - start_samples) * (1 - probs)
        log_start_samples_idx = torch.log(start_samples_idx)
        log_start_samples = log_start_samples_idx.sum(dim=1)
        loss_ls = torch.mean(log_start_samples * res_samples)
        loss = loss_ls + alpha * reg

        # 3. 返回包含所有信息的字典
        retdict["output"] = [probs.squeeze(-1), "hist"]
        retdict["reg"] = [reg, "sequence"]
        retdict["loss"] = [loss, "sequence"]
        return retdict

    def __repr__(self):
        return self.__class__.__name__

# ==============================================================================
#  新增的 Transformer 模型
# ==============================================================================
class TransformerModel(nn.Module):
    def __init__(self, nvar, embedding_dim, num_heads, num_layers, dim_feedforward, dropout=0.1):
        super(TransformerModel, self).__init__()
        self.nvar = nvar
        
        # 1. 节点嵌入层: 为每个变量创建一个可学习的向量
        self.embedding = nn.Embedding(nvar, embedding_dim)
        
        # 2. Transformer 编码器层: 这是模型的核心
        # 我们使用 TransformerEncoder 因为我们是对所有节点并行处理，而非自回归生成
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embedding_dim,
            nhead=num_heads,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True # 使用 (batch, seq, feature) 格式
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # 3. 输出层: 将Transformer的输出映射回每个变量的概率
        self.output_layer = nn.Linear(embedding_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def reset_parameters(self):
        self.embedding.reset_parameters()
        self.output_layer.reset_parameters()
        # 重置Transformer编码器层
        for layer in self.transformer_encoder.layers:
            layer.self_attn.in_proj_weight.data.normal_(0, 0.02)
            layer.self_attn.out_proj.weight.data.normal_(0, 0.02)
            layer.linear1.weight.data.normal_(0, 0.02)
            layer.linear2.weight.data.normal_(0, 0.02)

    def _create_attention_mask(self, data, device):
        # 创建一个基于图邻接关系的注意力掩码
        # 掩码值为0.0表示允许关注，-inf表示禁止关注
        adj = torch.full((self.nvar, self.nvar), float('-inf'), device=device)
        
        # 允许节点关注自己
        adj.fill_diagonal_(0.0)
        
        # 允许节点关注它的邻居
        edge_index = data.edge_index
        adj[edge_index[0], edge_index[1]] = 0.0
        adj[edge_index[1], edge_index[0]] = 0.0 # 无向图
        
        return adj

    def forward(self, data, alpha=0.1, start_samples=None, value=None, 
                device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
        
        # ================= Part 1: 生成概率 (升级后的"大脑") =================
        # 1.1 获取所有节点的初始嵌入
        node_indices = torch.arange(self.nvar, device=device)
        x = self.embedding(node_indices).unsqueeze(0) # 增加 batch 维度

        # 1.2 创建注意力掩码，将图结构注入模型
        # 只在Max-Cut这类图问题上创建掩码
        attn_mask = None
        if hasattr(data, 'edge_index'):
             attn_mask = self._create_attention_mask(data, device)

        # 1.3 通过Transformer进行信息交换
        transformer_output = self.transformer_encoder(x, mask=attn_mask)
        
        # 1.4 生成最终概率
        logits = self.output_layer(transformer_output).squeeze(0).squeeze(-1)
        probs = self.sigmoid(logits)

                # ================= Part 2: 计算损失（稳定版 + 形状修复） =================
        retdict = {}

        # 先准备概率与熵正则（稳定写法）
        p = torch.sigmoid(logits)  # [nvar]
        log_p = -F.softplus(-logits)
        log_q = -F.softplus( logits)
        entropy = -(p * log_p + (1 - p) * log_q)   # 标准伯努利熵（稳定）
        reg = -entropy.mean()  # 和你原本 reg 定义一致

        if start_samples is None:
            retdict["output"] = [p, "hist"]
            retdict["reg"]    = [reg, "sequence"]
            retdict["loss"]   = [alpha * reg, "sequence"]
            return retdict

        # ---- 关键修复：把 logits 扩成 [B, nvar] 与 start_samples 对齐 ----
        B = start_samples.shape[0]          # [B, nvar]
        logits_batched = logits.unsqueeze(0).expand(B, -1)  # [B, nvar]

        # 用 BCEWithLogits 计算每个节点的 log-prob（稳定，不会 log(0)）
        log_p_node = -F.binary_cross_entropy_with_logits(
            logits_batched, start_samples.float(), reduction='none'
        )  # [B, nvar]

        log_start_samples = log_p_node.sum(dim=1)                 # [B]
        log_start_samples = torch.nan_to_num(log_start_samples, neginf=-1e9, posinf=1e9)

        res_samples = value.t().detach()                          # [B]
        res_samples = torch.nan_to_num(res_samples, nan=0.0, neginf=0.0, posinf=0.0)

        loss_ls = torch.mean(log_start_samples * res_samples)
        loss = loss_ls + alpha * reg

        retdict["output"] = [p, "hist"]       # 这里仍返回按节点的概率 [nvar]
        retdict["reg"]    = [reg, "sequence"]
        retdict["loss"]   = [loss, "sequence"]
        return retdict


    def __repr__(self):
        return self.__class__.__name__