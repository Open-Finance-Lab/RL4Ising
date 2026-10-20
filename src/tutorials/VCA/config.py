import tensorflow as tf
from math import sqrt 
import numpy as np

class config:
    def __init__(self, graph_path, seed):
        N, Jz = self.read_graph(graph_path)
        self.seed = seed

        self.N = N #total number of sites
        self.Jz = Jz

        '''model'''
        self.num_units = 40                     # number of memory units
        self.num_layers = int(sqrt(N))          # number of layers 
        self.activation_function = tf.nn.elu    # non-linear activation function for the RNN cell

        '''training'''
        self.numsamples = 50            # number of samples used for training
        self.lr = 5*(1e-4)              # learning rate
        self.T0 = 2                     # Initial temperature
        self.Bx0 = 0                    # Initial magnetic field
        self.num_warmup_steps = 1000    # number of warmup steps
        self.num_annealing_steps = 2**8 # number of annealing steps
        self.num_equilibrium_steps = 5  # number of training steps after each annealing step
    
    def read_graph(self, graph_path):

        with open(graph_path, "r") as f:
            line = f.readline()
            is_first_line = True
            while line is not None and line != '':
                if is_first_line:
                    nodes, edges = line.strip().split(" ")
                    num_nodes = int(nodes)
                    num_edges = int(edges)
                    is_first_line = False
                    Jz = np.zeros((num_nodes, num_nodes), dtype=np.float64)
                else:
                    node1, node2, weight = line.strip().split(" ")
                    Jz[(int(node1)-1, int(node2)-1)] = float(weight)
                    Jz[(int(node2)-1, int(node1)-1)] = float(weight)
                line = f.readline()
        return num_nodes, Jz