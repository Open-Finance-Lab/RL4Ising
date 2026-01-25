import networkx as nx
import base64

def read_nxgraph(filename: str) -> nx.Graph(): # type: ignore
    graph = nx.Graph()
    with open(filename, 'r') as file:
        # lines = []
        line = file.readline()
        is_first_line = True
        while line is not None and line != '':
            if '//' not in line:
                if is_first_line:
                    strings = line.split(" ")
                    num_nodes = int(strings[0])
                    num_edges = int(strings[1])
                    nodes = list(range(num_nodes))
                    graph.add_nodes_from(nodes)
                    is_first_line = False
                else:
                    node1, node2, weight = line.split()
                    graph.add_edge(int(node1), int(node2), weight=weight)
            line = file.readline()
    return graph

def float_to_binary(variable):
    return f"{int(variable)}"

def base64_encode(solution):
    bytes = int(solution, base=2).to_bytes((len(solution) + 7) // 8, byteorder='big')
    encoded_str = base64.b64encode(bytes).decode("utf-8")
    return encoded_str