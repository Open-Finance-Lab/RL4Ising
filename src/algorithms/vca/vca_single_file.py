import tensorflow as tf
import numpy as np
import argparse
from math import sqrt
import os
import time
import random
from natsort import natsorted
from typing import Any, Optional, Union, Text, Sequence, Tuple, List

Tensor = Any

'''
Config
'''
class Config:
    def __init__(self, graph_path, seed):
        Nx, Ny, Jz = self.read_graph(graph_path)
        self.seed = seed

        self.Nx = Nx
        self.Ny = Ny
        self.N = Nx*Ny #total number of sites
        self.Jz = Jz

        '''model'''
        self.num_units = 40 #number of memory units
        self.activation_function = tf.nn.elu #non-linear activation function for the 2D Tensorized RNN cell

        '''training'''
        self.numsamples = 50 #number of samples used for training
        self.lr = 5*(1e-4) #learning rate
        self.T0 = 2 #Initial temperature
        self.Bx0 = 0 #Initial magnetic field
        self.num_warmup_steps = 1000 #number of warmup steps
        self.num_annealing_steps = 2**8 #number of annealing steps
        self.num_equilibrium_steps = 5 #number of training steps after each annealing step
    
    def read_graph(self, graph_path):
        edge_list = dict()
        with open(graph_path, "r") as f:
            line = f.readline()
            is_first_line = True
            while line is not None and line != '':
                if is_first_line:
                    nodes, edges = line.split(" ")
                    num_nodes = int(nodes)
                    num_edges = int(edges)
                    is_first_line = False
                else:
                    node1, node2, weight = line.split(" ")
                    edge_list[(int(node1), int(node2))] = float(weight)
                line = f.readline()

        Nx = int(sqrt(num_nodes))
        Ny = Nx
        Jz = np.zeros((Nx, Ny, 2), dtype=np.float64)
        for i in range(Nx):
            for j in range(Ny):
                if i != Nx-1:
                    right = edge_list.get((i+j*Ny+1, i+1+j*Ny+1))
                    if right is not None:
                       Jz[i, j, 0] = right
                if j != Ny-1:
                    down = edge_list.get((i+j*Ny+1, i+(j+1)*Ny+1))
                    if down is not None:
                       Jz[i, j, 1] = down
        return Nx, Ny, Jz
    
'''
Network
'''
class MDRNNWavefunction(object):
    def __init__(self,systemsize_x = None, systemsize_y = None,cell=None,activation=None,num_units = None,scope='RNNWavefunction',seed = 111):
        self.graph=tf.Graph()
        self.scope=scope #Label of the RNN wavefunction
        self.Nx=systemsize_x
        self.Ny=systemsize_y

        random.seed(seed)  # `python` built-in pseudo-random generator
        np.random.seed(seed)  # numpy pseudo-random generator

        #Defining the neural network
        with self.graph.as_default():
            with tf.variable_scope(self.scope,reuse=tf.AUTO_REUSE):

              tf.set_random_seed(seed)  # tensorflow pseudo-random generator

              #Defining the 2D Tensorized RNN cell with non-weight sharing
              self.rnn=[cell(num_units = num_units, activation = activation, name="rnn_"+str(0)+str(i),dtype=tf.float64) for i in range(self.Nx*self.Ny)]
              self.dense = [tf.layers.Dense(2,activation=tf.nn.softmax,name='wf_dense'+str(i), dtype = tf.float64) for i in range(self.Nx*self.Ny)]

    def sample(self,numsamples,inputdim):
        with self.graph.as_default(): #Call the default graph, used if willing to create multiple graphs.
            with tf.variable_scope(self.scope,reuse=tf.AUTO_REUSE):
                self.inputdim=inputdim
                self.outputdim=self.inputdim
                self.numsamples=numsamples

                samples=[[[] for nx in range(self.Nx)] for ny in range(self.Ny)]
                probs = [[[] for nx in range(self.Nx)] for ny in range(self.Ny)]
                rnn_states = {}
                inputs = {}

                for ny in range(self.Ny): #Loop over the boundaries for initialization
                    if ny%2==0:
                        nx = -1
                        # print(nx,ny)
                        rnn_states[str(nx)+str(ny)]=self.rnn[0].zero_state(self.numsamples,dtype=tf.float64)
                        inputs[str(nx)+str(ny)] = tf.zeros((self.numsamples,inputdim), dtype = tf.float64) #Feed the table b in tf.

                    if ny%2==1:
                        nx = self.Nx
                        # print(nx,ny)
                        rnn_states[str(nx)+str(ny)]=self.rnn[0].zero_state(self.numsamples,dtype=tf.float64)
                        inputs[str(nx)+str(ny)] = tf.zeros((self.numsamples,inputdim), dtype = tf.float64) #Feed the table b in tf.


                for nx in range(self.Nx): #Loop over the boundaries for initialization
                    ny = -1
                    rnn_states[str(nx)+str(ny)]=self.rnn[0].zero_state(self.numsamples,dtype=tf.float64)
                    inputs[str(nx)+str(ny)] = tf.zeros((self.numsamples,inputdim), dtype = tf.float64) #Feed the table b in tf.

                #Making a loop over the sites with the 2DRNN
                for ny in range(self.Ny):

                    if ny%2 == 0:

                        for nx in range(self.Nx): #left to right

                            rnn_output, rnn_states[str(nx)+str(ny)] = self.rnn[ny*self.Nx+nx]((inputs[str(nx-1)+str(ny)],inputs[str(nx)+str(ny-1)]), (rnn_states[str(nx-1)+str(ny)],rnn_states[str(nx)+str(ny-1)]))

                            output=self.dense[ny*self.Nx+nx](rnn_output)
                            sample_temp=tf.reshape(tf.multinomial(tf.log(output),num_samples=1),[-1,])
                            samples[nx][ny] = sample_temp
                            probs[nx][ny] = output
                            inputs[str(nx)+str(ny)]=tf.one_hot(sample_temp,depth=self.outputdim, dtype = tf.float64)


                    if ny%2 == 1:

                        for nx in range(self.Nx-1,-1,-1): #right to left

                            rnn_output, rnn_states[str(nx)+str(ny)] = self.rnn[ny*self.Nx+nx]((inputs[str(nx+1)+str(ny)],inputs[str(nx)+str(ny-1)]), (rnn_states[str(nx+1)+str(ny)],rnn_states[str(nx)+str(ny-1)]))

                            output=self.dense[ny*self.Nx+nx](rnn_output)
                            sample_temp=tf.reshape(tf.multinomial(tf.log(output),num_samples=1),[-1,])
                            samples[nx][ny] = sample_temp
                            probs[nx][ny] = output
                            inputs[str(nx)+str(ny)]=tf.one_hot(sample_temp,depth=self.outputdim, dtype = tf.float64)


        self.samples=tf.transpose(tf.stack(values=samples,axis=0), perm = [2,0,1])

        probs=tf.transpose(tf.stack(values=probs,axis=0),perm=[2,0,1,3])
        one_hot_samples=tf.one_hot(self.samples,depth=self.inputdim, dtype = tf.float64)
        self.log_probs=tf.reduce_sum(tf.reduce_sum(tf.log(tf.reduce_sum(tf.multiply(probs,one_hot_samples),axis=3)),axis=2),axis=1)

        return self.samples,self.log_probs

    def log_probability(self,samples,inputdim):
        with self.graph.as_default():

            self.inputdim=inputdim
            self.outputdim=self.inputdim

            self.numsamples=tf.shape(samples)[0]

            #Initial input to feed to the lstm
            self.outputdim=self.inputdim


            samples_=tf.transpose(samples, perm = [1,2,0])
            rnn_states = {}
            inputs = {}

            for ny in range(self.Ny): #Loop over the boundaries for initialization
                if ny%2==0:
                    nx = -1
                    rnn_states[str(nx)+str(ny)]=self.rnn[0].zero_state(self.numsamples,dtype=tf.float64)
                    inputs[str(nx)+str(ny)] = tf.zeros((self.numsamples,inputdim), dtype = tf.float64) #Feed the table b in tf.

                if ny%2==1:
                    nx = self.Nx
                    rnn_states[str(nx)+str(ny)]=self.rnn[0].zero_state(self.numsamples,dtype=tf.float64)
                    inputs[str(nx)+str(ny)] = tf.zeros((self.numsamples,inputdim), dtype = tf.float64) #Feed the table b in tf.


            for nx in range(self.Nx): #Loop over the boundaries for initialization
                ny = -1
                rnn_states[str(nx)+str(ny)]=self.rnn[0].zero_state(self.numsamples,dtype=tf.float64)
                inputs[str(nx)+str(ny)] = tf.zeros((self.numsamples,inputdim), dtype = tf.float64) #Feed the table b in tf.


            with tf.variable_scope(self.scope,reuse=tf.AUTO_REUSE):
                probs = [[[] for nx in range(self.Nx)] for ny in range(self.Ny)]

                #Making a loop over the sites with the 2DRNN
                for ny in range(self.Ny):

                    if ny%2 == 0:

                        for nx in range(self.Nx): #left to right

                            rnn_output, rnn_states[str(nx)+str(ny)] = self.rnn[ny*self.Nx+nx]((inputs[str(nx-1)+str(ny)],inputs[str(nx)+str(ny-1)]), (rnn_states[str(nx-1)+str(ny)],rnn_states[str(nx)+str(ny-1)]))

                            output=self.dense[ny*self.Nx+nx](rnn_output)
                            sample_temp=tf.reshape(tf.multinomial(tf.log(output),num_samples=1),[-1,])
                            probs[nx][ny] = output
                            inputs[str(nx)+str(ny)]=tf.one_hot(samples_[nx,ny],depth=self.outputdim,dtype = tf.float64)

                    if ny%2 == 1:

                        for nx in range(self.Nx-1,-1,-1): #right to left

                            rnn_output, rnn_states[str(nx)+str(ny)] = self.rnn[ny*self.Nx+nx]((inputs[str(nx+1)+str(ny)],inputs[str(nx)+str(ny-1)]), (rnn_states[str(nx+1)+str(ny)],rnn_states[str(nx)+str(ny-1)]))

                            output=self.dense[ny*self.Nx+nx](rnn_output)
                            sample_temp=tf.reshape(tf.multinomial(tf.log(output),num_samples=1),[-1,])
                            probs[nx][ny] = output
                            inputs[str(nx)+str(ny)]=tf.one_hot(samples_[nx,ny],depth=self.outputdim,dtype = tf.float64)

            probs=tf.transpose(tf.stack(values=probs,axis=0),perm=[2,0,1,3])
            one_hot_samples=tf.one_hot(samples,depth=self.inputdim, dtype = tf.float64)

            self.log_probs=tf.reduce_sum(tf.reduce_sum(tf.log(tf.reduce_sum(tf.multiply(probs,one_hot_samples),axis=3)),axis=2),axis=1)

            return self.log_probs

class MDTensorizedRNNCell(tf.contrib.rnn.RNNCell):
    """The 2D Tensorized RNN cell.
    """
    def __init__(self, num_units = None, activation = None, name=None, dtype = None, reuse=None):
        super(MDTensorizedRNNCell, self).__init__(_reuse=reuse, name=name)
        # save class variables
        self._num_in = 2
        self._num_units = num_units
        self._state_size = num_units
        self._output_size = num_units
        self.activation = activation

        # set up input -> hidden connection
        self.W = tf.get_variable("W_"+name, shape=[num_units, 2*num_units, 2*self._num_in],
                                    initializer=tf.contrib.layers.xavier_initializer(), dtype = dtype)

        self.b = tf.get_variable("b_"+name, shape=[num_units],
                                    initializer=tf.contrib.layers.xavier_initializer(), dtype = dtype)

    @property
    def input_size(self):
        return self._num_in # real

    @property
    def state_size(self):
        return self._state_size # real

    @property
    def output_size(self):
        return self._output_size # real

    def call(self, inputs, states):

        inputstate_mul = tf.einsum('ij,ik->ijk', tf.concat(states, 1),tf.concat(inputs,1))
        # prepare input linear combination
        state_mul = tensordot(tf, inputstate_mul, self.W, axes=[[1,2],[1,2]]) # [batch_sz, num_units]

        preact = state_mul + self.b

        output = self.activation(preact) # [batch_sz, num_units] C

        new_state = output

        return output, new_state

def tensordot(tf,
              a,
              b,
              axes,
              name: Optional[Text] = None) -> Tensor:

  def _tensordot_should_flip(contraction_axes: List[int],
                             free_axes: List[int]) -> bool:
    # NOTE: This will fail if the arguments contain any Tensors.
    if contraction_axes and free_axes:
      return bool(np.mean(contraction_axes) < np.mean(free_axes))
    return False

  def _tranpose_if_necessary(tensor: Tensor, perm: List[int]) -> Tensor:
    if perm == list(range(len(perm))):
      return tensor
    return tf.transpose(tensor, perm)

  def _reshape_if_necessary(tensor: Tensor,
                            new_shape: List[int]) -> Tensor:
    cur_shape = tensor.get_shape().as_list()
    if (len(new_shape) == len(cur_shape) and
        all(d0 == d1 for d0, d1 in zip(cur_shape, new_shape))):
      return tensor
    return tf.reshape(tensor, new_shape)

  def _tensordot_reshape(
      a: Tensor, axes: Union[Sequence[int], Tensor], is_right_term=False
  ) -> Tuple[Tensor, Union[List[int], Tensor], Optional[List[int]], bool]:
    if a.get_shape().is_fully_defined() and isinstance(axes, (list, tuple)):
      shape_a = a.get_shape().as_list()
      # NOTE: This will fail if axes contains any tensors
      axes = [i if i >= 0 else i + len(shape_a) for i in axes]
      free = [i for i in range(len(shape_a)) if i not in axes]
      flipped = _tensordot_should_flip(axes, free)

      free_dims = [shape_a[i] for i in free]
      prod_free = int(np.prod([shape_a[i] for i in free]))
      prod_axes = int(np.prod([shape_a[i] for i in axes]))
      perm = axes + free if flipped else free + axes
      new_shape = [prod_axes, prod_free] if flipped else [prod_free, prod_axes]
      transposed_a = _tranpose_if_necessary(a, perm)
      reshaped_a = _reshape_if_necessary(transposed_a, new_shape)
      transpose_needed = (not flipped) if is_right_term else flipped
      return reshaped_a, free_dims, free_dims, transpose_needed
    if a.get_shape().ndims is not None and isinstance(axes, (list, tuple)):
      shape_a = a.get_shape().as_list()
      axes = [i if i >= 0 else i + len(shape_a) for i in axes]
      free = [i for i in range(len(shape_a)) if i not in axes]
      flipped = _tensordot_should_flip(axes, free)
      perm = axes + free if flipped else free + axes

      axes_dims = [shape_a[i] for i in axes]
      free_dims = [shape_a[i] for i in free]
      free_dims_static = free_dims
      axes = tf.convert_to_tensor(axes, dtype=tf.dtypes.int32, name="axes")
      free = tf.convert_to_tensor(free, dtype=tf.dtypes.int32, name="free")
      shape_a = tf.shape(a)
      transposed_a = _tranpose_if_necessary(a, perm)
    else:
      free_dims_static = None
      shape_a = tf.shape(a)
      rank_a = tf.rank(a)
      axes = tf.convert_to_tensor(axes, dtype=tf.dtypes.int32, name="axes")
      axes = tf.where(axes >= 0, axes, axes + rank_a)
      free, _ = tf.compat.v1.setdiff1d(tf.range(rank_a), axes)
      flipped = is_right_term
      perm = (
          tf.concat([axes, free], 0) if flipped else tf.concat([free, axes], 0))
      transposed_a = tf.transpose(a, perm)

    free_dims = tf.gather(shape_a, free)
    axes_dims = tf.gather(shape_a, axes)
    prod_free_dims = tf.reduce_prod(free_dims)
    prod_axes_dims = tf.reduce_prod(axes_dims)

    if flipped:
      new_shape = tf.stack([prod_axes_dims, prod_free_dims])
    else:
      new_shape = tf.stack([prod_free_dims, prod_axes_dims])
    reshaped_a = tf.reshape(transposed_a, new_shape)
    transpose_needed = (not flipped) if is_right_term else flipped
    return reshaped_a, free_dims, free_dims_static, transpose_needed

  def _tensordot_axes(a: Tensor, axes
                     ) -> Tuple[Any, Any]:
    """Generates two sets of contraction axes for the two tensor arguments."""
    a_shape = a.get_shape()
    if isinstance(axes, tf.compat.integral_types):
      if axes < 0:
        raise ValueError("'axes' must be at least 0.")
      if a_shape.ndims is not None:
        if axes > a_shape.ndims:
          raise ValueError("'axes' must not be larger than the number of "
                           "dimensions of tensor %s." % a)
        return (list(range(a_shape.ndims - axes,
                           a_shape.ndims)), list(range(axes)))
      rank = tf.rank(a)
      return (tf.range(rank - axes, rank,
                       dtype=tf.int32), tf.range(axes, dtype=tf.int32))
    if isinstance(axes, (list, tuple)):
      if len(axes) != 2:
        raise ValueError("'axes' must be an integer or have length 2.")
      a_axes = axes[0]
      b_axes = axes[1]
      if isinstance(a_axes, tf.compat.integral_types) and \
          isinstance(b_axes, tf.compat.integral_types):
        a_axes = [a_axes]
        b_axes = [b_axes]
      # NOTE: This fails if either a_axes and b_axes are Tensors.
      if len(a_axes) != len(b_axes):
        raise ValueError(
            "Different number of contraction axes 'a' and 'b', %s != %s." %
            (len(a_axes), len(b_axes)))

      # The contraction indices do not need to be permuted.
      # Sort axes to avoid unnecessary permutations of a.
      # NOTE: This fails if either a_axes and b_axes contain Tensors.
      # pylint: disable=len-as-condition
      if len(a_axes) > 0:
        a_axes, b_axes = list(zip(*sorted(zip(a_axes, b_axes))))

      return a_axes, b_axes
    axes = tf.convert_to_tensor(axes, name="axes", dtype=tf.int32)
    return axes[0], axes[1]

  with tf.compat.v1.name_scope(name, "Tensordot", [a, b, axes]) as _name:
    a = tf.convert_to_tensor(a, name="a")
    b = tf.convert_to_tensor(b, name="b")
    a_axes, b_axes = _tensordot_axes(a, axes)
    a_reshape, a_free_dims, a_free_dims_static, a_transp = _tensordot_reshape(
        a, a_axes)
    b_reshape, b_free_dims, b_free_dims_static, b_transp = _tensordot_reshape(
        b, b_axes, is_right_term=True)

    ab_matmul = tf.matmul(
        a_reshape, b_reshape, transpose_a=a_transp, transpose_b=b_transp)

    if isinstance(a_free_dims, list) and isinstance(b_free_dims, list):
      return tf.reshape(ab_matmul, a_free_dims + b_free_dims, name=_name)
    a_free_dims = tf.convert_to_tensor(a_free_dims, dtype=tf.dtypes.int32)
    b_free_dims = tf.convert_to_tensor(b_free_dims, dtype=tf.dtypes.int32)
    product = tf.reshape(
        ab_matmul, tf.concat([a_free_dims, b_free_dims], 0), name=_name)
    if a_free_dims_static is not None and b_free_dims_static is not None:
      product.set_shape(a_free_dims_static + b_free_dims_static)
    return product
  
'''
Utils
'''
def Ising2D_diagonal_matrixelements(Jz, samples):
    numsamples = samples.shape[0]
    Nx = samples.shape[1]
    Ny = samples.shape[2]

    N = Nx*Ny #Total number of spins

    local_energies = np.zeros((numsamples), dtype = np.float64)

    for i in range(Nx-1): #diagonal elements (right neighbours)
        values = samples[:,i]+samples[:,i+1]
        valuesT = np.copy(values)
        valuesT[values==2] = +1 #If both spins are up
        valuesT[values==0] = +1 #If both spins are down
        valuesT[values==1] = -1 #If they are opposite

        local_energies += np.sum(valuesT*(-Jz[i,:,0]), axis = 1)

    for i in range(Ny-1): #diagonal elements (upward neighbours (or downward, it depends on the way you see the lattice :)))
        values = samples[:,:,i]+samples[:,:,i+1]
        valuesT = np.copy(values)
        valuesT[values==2] = +1 #If both spins are up
        valuesT[values==0] = +1 #If both spins are down
        valuesT[values==1] = -1 #If they are opposite

        local_energies += np.sum(valuesT*(-Jz[:,i,1]), axis = 1)

    return local_energies

def Ising2D_local_energies(Jz, Bx, samples, queue_samples, log_probs_tensor, samples_placeholder, log_probs, sess):
    numsamples = samples.shape[0]
    Nx = samples.shape[1]
    Ny = samples.shape[2]

    N = Nx*Ny #Total number of spins

    local_energies = np.zeros((numsamples), dtype = np.float64)

    for i in range(Nx-1): #diagonal elements (right neighbours)
        values = samples[:,i]+samples[:,i+1]
        valuesT = np.copy(values)
        valuesT[values==2] = +1 #If both spins are up
        valuesT[values==0] = +1 #If both spins are down
        valuesT[values==1] = -1 #If they are opposite

        local_energies += np.sum(valuesT*(-Jz[i,:,0]), axis = 1)

    for i in range(Ny-1): #diagonal elements (upward neighbours (or downward, it depends on the way you see the lattice :)))
        values = samples[:,:,i]+samples[:,:,i+1]
        valuesT = np.copy(values)
        valuesT[values==2] = +1 #If both spins are up
        valuesT[values==0] = +1 #If both spins are down
        valuesT[values==1] = -1 #If they are opposite

        local_energies += np.sum(valuesT*(-Jz[:,i,1]), axis = 1)


    queue_samples[0] = samples #storing the diagonal samples

    if Bx != 0:
        for i in range(Nx):  #Non-diagonal elements
            for j in range(Ny):
                valuesT = np.copy(samples)
                valuesT[:,i,j][samples[:,i,j]==1] = 0 #Flip
                valuesT[:,i,j][samples[:,i,j]==0] = 1 #Flip

                queue_samples[i*Ny+j+1] = valuesT

        len_sigmas = (N+1)*numsamples
        steps = len_sigmas//50000+1 #I want a maximum in batch size just to not allocate too much memory
        # print("Total num of steps =", steps)
        queue_samples_reshaped = np.reshape(queue_samples, [(N+1)*numsamples, Nx,Ny])
        for i in range(steps):
          if i < steps-1:
              cut = slice((i*len_sigmas)//steps,((i+1)*len_sigmas)//steps)
          else:
              cut = slice((i*len_sigmas)//steps,len_sigmas)
          log_probs[cut] = sess.run(log_probs_tensor, feed_dict={samples_placeholder:queue_samples_reshaped[cut]})

        log_probs_reshaped = np.reshape(log_probs, [N+1,numsamples])
        for j in range(numsamples):
            local_energies[j] += -Bx*np.sum(np.exp(0.5*log_probs_reshaped[1:,j]-0.5*log_probs_reshaped[0,j]))

    return local_energies

'''
Variational Classical Annealing
'''
def run_vca(config: Config):
    seed = config.seed
    tf.compat.v1.reset_default_graph()
    random.seed(seed)  # `python` built-in pseudo-random generator
    np.random.seed(seed)  # numpy pseudo-random generator
    tf.compat.v1.set_random_seed(seed)  # tensorflow pseudo-random generator

    Nx = config.Nx
    Ny = config.Ny
    N = config.N
    Jz = config.Jz

    num_units = config.num_units
    activation_function = config.activation_function

    numsamples = config.numsamples
    lr = config.lr
    T0 = config.T0
    Bx0 = config.Bx0
    num_warmup_steps = config.num_warmup_steps
    num_annealing_steps = config.num_annealing_steps
    num_equilibrium_steps = config.num_equilibrium_steps

    print('\n')
    print("Number of spins =", N)
    print("Initial_temperature =", T0)
    print('Seed = ', seed)

    num_steps = num_annealing_steps*num_equilibrium_steps + num_warmup_steps

    print("\nNumber of annealing steps = {0}".format(num_annealing_steps))
    print("Number of training steps = {0}".format(num_steps))

    MDRNNWF = MDRNNWavefunction(systemsize_x = Nx, systemsize_y = Ny ,num_units = num_units,cell=MDTensorizedRNNCell, activation = activation_function, seed = seed) #contains the graph with the RNNs
    with tf.compat.v1.variable_scope(MDRNNWF.scope,reuse=tf.compat.v1.AUTO_REUSE):
        with MDRNNWF.graph.as_default():

            global_step = tf.Variable(0, trainable=False)
            learningrate_placeholder = tf.compat.v1.placeholder(dtype=tf.float64,shape=[])
            learningrate = tf.compat.v1.train.exponential_decay(learningrate_placeholder, global_step, 100, 1.0, staircase=True)

            #Defining the optimizer
            optimizer=tf.compat.v1.train.AdamOptimizer(learning_rate=learningrate)

            #Defining Tensorflow placeholders
            Eloc=tf.compat.v1.placeholder(dtype=tf.float64,shape=[numsamples])
            sampleplaceholder_forgrad=tf.compat.v1.placeholder(dtype=tf.int32,shape=[numsamples,Nx,Ny])
            log_probs_forgrad = MDRNNWF.log_probability(sampleplaceholder_forgrad,inputdim=2)

            samples_placeholder=tf.compat.v1.placeholder(dtype=tf.int32,shape=(None,Nx, Ny))
            log_probs_tensor=MDRNNWF.log_probability(samples_placeholder,inputdim=2)
            samplesandprobs = MDRNNWF.sample(numsamples=numsamples,inputdim=2)

            T_placeholder = tf.compat.v1.placeholder(dtype=tf.float64,shape=())

            #Here we define a fake cost function that would allows to get the gradients of free energy using the tf.stop_gradient trick
            Floc = Eloc + T_placeholder*log_probs_forgrad
            cost = tf.reduce_mean(tf.multiply(log_probs_forgrad,tf.stop_gradient(Floc))) - tf.reduce_mean(log_probs_forgrad)*tf.reduce_mean(tf.stop_gradient(Floc))

            gradients, variables = zip(*optimizer.compute_gradients(cost))

            optstep=optimizer.apply_gradients(zip(gradients,variables), global_step = global_step)

            saver=tf.compat.v1.train.Saver()

            init=tf.compat.v1.global_variables_initializer()
            initialize_parameters = tf.initialize_all_variables()

    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True

    sess=tf.compat.v1.Session(graph=MDRNNWF.graph, config=config)
    sess.run(init)

    ## Run Variational Annealing
    with tf.compat.v1.variable_scope(MDRNNWF.scope,reuse=tf.compat.v1.AUTO_REUSE):
        with MDRNNWF.graph.as_default():
            #To store data
            meanEnergy=[]
            varEnergy=[]
            varFreeEnergy = []
            meanFreeEnergy = []
            samples = np.ones((numsamples, Nx, Ny), dtype=np.int32)
            queue_samples = np.zeros((N+1, numsamples, Nx, Ny), dtype = np.int32)
            log_probs = np.zeros((N+1)*numsamples, dtype=np.float64) 

            T = T0 #initializing temperature
            Bx = Bx0 #initializing magnetic field

            sess.run(initialize_parameters) #Reinitialize the parameters

            start = time.time()
            for it in range(len(meanEnergy),num_steps+1):
                #Annealing
                if it>=num_warmup_steps and  it <= num_annealing_steps*num_equilibrium_steps + num_warmup_steps and it % num_equilibrium_steps == 0:
                    annealing_step = (it-num_warmup_steps)/num_equilibrium_steps
                    T = T0*(1-annealing_step/num_annealing_steps)
                    Bx = Bx0*(1-annealing_step/num_annealing_steps)

                #Showing current status after that the annealing starts
                if it%num_equilibrium_steps==0:
                    if it <= num_annealing_steps*num_equilibrium_steps + num_warmup_steps and it>=num_warmup_steps:
                        annealing_step = (it-num_warmup_steps)/num_equilibrium_steps
                        print("\nAnnealing step: {0}/{1}".format(annealing_step,num_annealing_steps))

                samples, log_probabilities = sess.run(samplesandprobs)

                # Estimating the local energies
                local_energies = Ising2D_local_energies(Jz, Bx, samples, queue_samples, log_probs_tensor, samples_placeholder, log_probs, sess)

                meanE = np.mean(local_energies)
                varE = np.var(local_energies)

                #adding elements to be saved
                meanEnergy.append(meanE)
                varEnergy.append(varE)

                meanF = np.mean(local_energies+T*log_probabilities)
                varF = np.var(local_energies+T*log_probabilities)

                meanFreeEnergy.append(meanF)
                varFreeEnergy.append(varF)

                if it%num_equilibrium_steps==0:
                    print('mean(E): {0}, mean(F): {1}, var(E): {2}, var(F): {3}, #samples {4}, #Training step {5}'.format(meanE,meanF,varE,varF,numsamples, it))
                    print("Temperature: ", T)
                    print("Magnetic field: ", Bx)

                #Here we produce samples at the end of annealing
                if it == num_annealing_steps*num_equilibrium_steps + num_warmup_steps:

                    Nsteps = 20
                    numsamples_estimation = 10**6 #Num samples to be obtained at the end
                    numsamples_perstep = numsamples_estimation//Nsteps #The number of steps taken to get "numsamples_estimation" samples (to avoid memory allocation issues)

                    samplesandprobs_final = MDRNNWF.sample(numsamples=numsamples_perstep,inputdim=2)
                    energies = np.zeros((numsamples_estimation))
                    solutions = np.zeros((numsamples_estimation, Nx, Ny))
                    print("\nSaving energy and variance before the end of annealing")

                    for i in range(Nsteps):
                        # print("\nsampling started")
                        samples_final, _ = sess.run(samplesandprobs_final)
                        # print("\nsampling finished")
                        energies[i*numsamples_perstep:(i+1)*numsamples_perstep] = Ising2D_diagonal_matrixelements(Jz,samples_final)
                        solutions[i*numsamples_perstep:(i+1)*numsamples_perstep] = samples_final
                        print("Sampling step:" , i+1, "/", Nsteps)
                    print("meanE = ", np.mean(energies))
                    print("varE = ", np.var(energies))
                    print("minE = ",np.min(energies))
                    return np.mean(energies), np.min(energies)

                #Run gradient descent step
                sess.run(optstep,feed_dict={Eloc:local_energies, sampleplaceholder_forgrad: samples, learningrate_placeholder: lr, T_placeholder:T})

                if it%5 == 0:
                    print("Elapsed time is =", time.time()-start, " seconds")
                    print('\n\n')
            
            

'''
Run VCA
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_instance", type=str,
                        help="input the data file for the problem instance")

    args = parser.parse_args()
    data_dir = args.problem_instance
    input_files = [ f for f in os.listdir(data_dir) ]
    input_files = natsorted(input_files)

    results_dir = f"results/{'/'.join(data_dir.split('/')[1:])}"
    os.makedirs(results_dir, exist_ok=True)

    i = 0
    for file in input_files:
        i += 1
        if i > 25: break
        # if i > 1: break

        vca_config = Config(f'{data_dir}/{file}', i)
        vca_config.num_units = 40
        vca_config.numsamples = 50
        vca_config.T0 = 1
        vca_config.lr = 5*(1e-4)
        vca_config.num_warmup_steps = 1000

        mean_energies, min_energies = run_vca(vca_config)

        with open(f"{results_dir}/VCA.txt", "a") as f:
            f.write(f"{min_energies}\n")
