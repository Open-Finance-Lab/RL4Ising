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
import yaml
import argparse
import time

from dataloader import dataloader_select
from model import simple
from sampling import sampler_select, sample_initializer


def mcpg_solver(nvar, config, data, verbose=False):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    sampler = sampler_select(config["problem_type"])
    change_times = int(nvar/10)  # transition times for metropolis sampling

    net = simple(nvar)
    net.to(device).reset_parameters()
    optimizer = torch.optim.Adam(net.parameters(), lr=config['lr_init'])

    start_samples = None
    for epoch in range(config['max_epoch_num']):

        if epoch % config['reset_epoch_num'] == 0:
            net.to(device).reset_parameters()
            regular = config['regular_init']

        net.train()
        if epoch <= 0:
            retdict = net(regular, None, None)
        else:
            retdict = net(regular, start_samples, value)

        retdict["loss"][0].backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(), 1)
        optimizer.step()

        # get start samples
        if epoch == 0:
            probs = (torch.zeros(nvar)+0.5).to(device)
            tensor_probs = sample_initializer(
                config["problem_type"], probs, config, data=data)
            temp_min, temp_min_info, temp_start_samples, value = sampler(
                data, tensor_probs, probs, config['num_ls'], 0, config['total_mcmc_num'])
            now_min_res = temp_min
            now_min_info = temp_min_info
            tensor_probs = temp_min_info.clone()
            tensor_probs = tensor_probs.repeat(1, config['repeat_times'])
            start_samples = temp_start_samples.t().to(device)

        # get samples
        if epoch % config['sample_epoch_num'] == 0 and epoch > 0:
            probs = retdict["output"][0]
            probs = probs.detach()
            temp_min, temp_min_info, start_samples_temp, value = sampler(
                data, tensor_probs, probs, config['num_ls'], change_times, config['total_mcmc_num'])
            # update now_max
            for i0 in range(config['total_mcmc_num']):
                if temp_min[i0] < now_min_res[i0]:
                    now_min_res[i0] = temp_min[i0]
                    now_min_info[:, i0] = temp_min_info[:, i0]

            # update if min is too small
            now_min = min(now_min_res).item()
            now_min_index = torch.argmax(now_min_res)
            now_max = max(now_min_res).item()
            now_max_index = torch.argmin(now_min_res)
            now_min_res[now_min_index] = now_min
            now_min_info[:, now_max_index] = now_min_info[:, now_min_index]
            temp_min_info[:, now_max_index] = now_min_info[:, now_min_index]

            # select best samples
            tensor_probs = temp_min_info.clone()
            tensor_probs = tensor_probs.repeat(1, config['repeat_times'])
            # construct the start point for next iteration
            start_samples = start_samples_temp.t()
            if verbose:
                print("o {:.3f}".format((min(now_min_res).item())))
        del (retdict)

    total_min = now_min_res
    best_sort = torch.argsort(now_min_res, descending=False)
    total_best_info = torch.squeeze(now_min_info[:, best_sort[0]])

    return min(total_min).item(), total_best_info, now_min_res, now_min_info

if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str,
                        help="input the configuration file for the mcpg solver")
    parser.add_argument("problem_instance", type=str,
                        help="input the data file for the problem instance")

    args = parser.parse_args()
    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    path = args.problem_instance
    start_time = time.perf_counter()
    dataloader = dataloader_select(config["problem_type"])
    data, nvar = dataloader(path)
    dataloader_t = time.perf_counter()
    res, solutions, _, _ = mcpg_solver(nvar, config, data, verbose=True)
    mcpg_t = time.perf_counter()


    print("OUTPUT: {:f}".format(res))
    print("DATA LOADING TIME: {:.4f}".format(dataloader_t - start_time))
    print("MCPG RUNNING TIME: {:.4f}".format(mcpg_t - dataloader_t))
