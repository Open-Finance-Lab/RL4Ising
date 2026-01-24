import torch
from torch_scatter import scatter
from torch.distributions.bernoulli import Bernoulli


def sample_initializer(problem_type, probs, config,
                       device=torch.device('cuda' if torch.cuda.is_available() else 'cpu'), data=None):
    if problem_type in ["r_cheegercut", "n_cheegercut"]:
        samples = torch.zeros(config['total_mcmc_num'], data.num_nodes)
        index = data.sorted_degree_nodes[- config['total_mcmc_num']:]
        for i in range(config['total_mcmc_num']):
            samples[i][index[i]] = 1
        samples = samples.repeat(config['repeat_times'], 1)
        return samples.t()
    m = Bernoulli(probs)
    samples = m.sample([config['total_mcmc_num'] * config['repeat_times']])
    samples = samples.detach().to(device)
    return samples.t()


def sampler_select(problem_type):
    if problem_type == "ising":
        return mcpg_sampling_ising
    else:
        raise (Exception("Unrecognized problem type {}".format(problem_type)))


def metro_sampling(probs, start_status, max_transfer_time,
                   device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    num_node = len(probs)
    num_chain = start_status.shape[1]
    index_col = torch.tensor(list(range(num_chain))).to(device)

    probs = probs.detach().to(device)
    samples = start_status.bool().to(device)

    count = 0
    for t in range(max_transfer_time * 5):
        if count >= num_chain*max_transfer_time:
            break
        index_row = torch.randint(low=0, high=num_node, size=[
                                  num_chain], device=device)
        chosen_probs_base = probs[index_row]
        chosen_value = samples[index_row, index_col]
        chosen_probs = torch.where(
            chosen_value, chosen_probs_base, 1-chosen_probs_base)
        accept_rate = (1 - chosen_probs) / chosen_probs
        r = torch.rand(num_chain, device=device)
        is_accept = (r < accept_rate)
        samples[index_row, index_col] = torch.where(
            is_accept, ~chosen_value, chosen_value)

        count += is_accept.sum()

    return samples.float().to(device)


def mcpg_sampling_ising(data,
                         start_result, probs,
                         num_ls, change_times, total_mcmc_num,
                         device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    probs = probs.to(torch.device("cpu"))
    num_edges = data.num_edges
    edges = data.edge_index
    nlr_graph = edges[0]
    nlc_graph = edges[1]
    edge_weight = data.edge_attr
    edge_weight_sum = data.edge_weight_sum
    graph_probs = start_result.clone()
    # get probs
    graph_probs = metro_sampling(
        probs, graph_probs, change_times, device)
    start = graph_probs.clone()

    temp = graph_probs[data.sorted_degree_nodes[0]].clone()
    graph_probs += temp
    graph_probs = graph_probs % 2

    graph_probs = (graph_probs - 0.5) * 2 + 0.5

    # local search
    temp = torch.zeros(4, graph_probs.size(dim=1)).to(device)
    expected_cut = torch.zeros(graph_probs.size(dim=1))
    cnt = 0
    while True:
        cnt += 1
        for i in range(num_edges):
            index = data.sorted_degree_edges[i]
            node_r = nlr_graph[index]
            node_c = nlc_graph[index]
            edges_r = data.n0_edges[index]
            edges_c = data.n1_edges[index]
            add_0 = data.add[0][index]
            add_1 = data.add[1][index]
            add_2 = data.add[2][index]

            temp_r_v = torch.mm(edges_r, graph_probs[data.n0[index]])
            temp_c_v = torch.mm(edges_c, graph_probs[data.n1[index]])

            temp[1] = temp_r_v + torch.rand(graph_probs.size(dim=1), device=device) * 0.1 + add_0
            temp[2] = temp_c_v + torch.rand(graph_probs.size(dim=1), device=device) * 0.1 + add_1
            temp[0] = temp[1] + temp[2] + torch.rand(graph_probs.size(dim=1),
                                                     device=torch.device(device)) * 0.1 - add_2

            max_index = torch.argmax(temp, dim=0)
            graph_probs[node_r] = torch.floor(max_index / 2)
            graph_probs[node_c] = max_index % 2

        if cnt >= num_ls:
            break

    # Convert Spins back to Ising model convention of -1 or +1
    spins = 2 * graph_probs - 1  # [nvar, chains]

    # Compute raw energy per chain: E(s) = - sum J_ij s_i s_j
    energy_vec = (edge_weight * (spins[nlr_graph] * spins[nlc_graph])).sum(dim=0)  # [chains]

    # full‐chain advantage for policy gradient
    adv = (energy_vec - energy_vec.mean()).to(device)  # [chains]

    # pick the best chain out of each repeat group
    energy_reshape = energy_vec.view(-1, total_mcmc_num)  # [repeat_times, total_mcmc_num]
    idx = torch.argmin(energy_reshape, dim=0)  # [total_mcmc_num]
    for i0 in range(total_mcmc_num):
            idx[i0] = i0 + idx[i0] * total_mcmc_num
    temp_min = energy_vec[idx]  # [total_mcmc_num] 
    temp_min_info = graph_probs[:, idx]  # [nvar, total_mcmc_num]
    start_samples = start  # [nvar, chains]
    
    # return best energy state, probs of the best energy states, the total probs, and the advantage 
    return temp_min, temp_min_info, start_samples, adv