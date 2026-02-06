import tensorflow as tf
import numpy as np
import argparse
import time
import random
from config import config
from DilatedRNN import DilatedRNNWavefunction
from utils import * 


def vca_solver(config: config):
    seed = config.seed
    tf.compat.v1.reset_default_graph()
    random.seed(seed)                   # `python` built-in pseudo-random generator
    np.random.seed(seed)                # numpy pseudo-random generator
    tf.compat.v1.set_random_seed(seed)  # tensorflow pseudo-random generator

    N = config.N
    Jz = config.Jz

    num_units = config.num_units
    num_layers = config.num_layers
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

    units = [num_units] * num_layers
    DRNNWF = DilatedRNNWavefunction(N, units=units, layers=num_layers, cell=tf.nn.rnn_cell.BasicRNNCell, activation=activation_function, seed=seed) # contains the graph with the RNNs
    with tf.compat.v1.variable_scope(DRNNWF.scope,reuse=tf.compat.v1.AUTO_REUSE):
        with DRNNWF.graph.as_default():

            global_step = tf.Variable(0, trainable=False)
            learningrate_placeholder = tf.compat.v1.placeholder(dtype=tf.float64,shape=[])
            learningrate = tf.compat.v1.train.exponential_decay(learningrate_placeholder, global_step, 100, 1.0, staircase=True)

            #Defining the optimizer
            optimizer=tf.compat.v1.train.AdamOptimizer(learning_rate=learningrate)

            #Defining Tensorflow placeholders
            Eloc=tf.compat.v1.placeholder(dtype=tf.float64,shape=[numsamples])
            sampleplaceholder_forgrad=tf.compat.v1.placeholder(dtype=tf.int32,shape=[numsamples,N])
            log_probs_forgrad = DRNNWF.log_probability(sampleplaceholder_forgrad,inputdim=2)
            samples_placeholder=tf.compat.v1.placeholder(dtype=tf.int32,shape=(None,N))
            log_probs_tensor=DRNNWF.log_probability(samples_placeholder,inputdim=2)
            samplesandprobs = DRNNWF.sample(numsamples=numsamples,inputdim=2)

            T_placeholder = tf.compat.v1.placeholder(dtype=tf.float64,shape=())

            #Here we define a fake cost function that would allows to get the gradients of free energy using the tf.stop_gradient trick
            Floc = Eloc + T_placeholder*log_probs_forgrad
            cost = tf.reduce_mean(tf.multiply(log_probs_forgrad,tf.stop_gradient(Floc))) - tf.reduce_mean(log_probs_forgrad)*tf.reduce_mean(tf.stop_gradient(Floc))

            gradients, variables = zip(*optimizer.compute_gradients(cost))
            #Calculate Gradients---------------

            #Define the optimization step
            optstep=optimizer.apply_gradients(zip(gradients,variables), global_step = global_step)

            #Tensorflow saver to checkpoint
            saver=tf.compat.v1.train.Saver()

            #For initialization
            init=tf.compat.v1.global_variables_initializer()
            initialize_parameters = tf.initialize_all_variables()

    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True

    sess=tf.compat.v1.Session(graph=DRNNWF.graph, config=config)
    sess.run(init)

    # Run Variational Annealing
    with tf.compat.v1.variable_scope(DRNNWF.scope,reuse=tf.compat.v1.AUTO_REUSE):
        with DRNNWF.graph.as_default():
            # To store data
            meanEnergy=[]
            varEnergy=[]
            varFreeEnergy = []
            meanFreeEnergy = []
            samples = np.ones((numsamples, N), dtype=np.int32)
            queue_samples = np.zeros((N+1, numsamples, N), dtype = np.int32)
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
                local_energies = Fullyconnected_localenergies(Jz, Bx, samples, queue_samples, log_probs_tensor, samples_placeholder, log_probs, sess)

                meanE = np.mean(local_energies)
                varE = np.var(local_energies)

                # adding elements to be saved
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
                    numsamples_estimation = 10**5 #Num samples to be obtained at the end
                    numsamples_perstep = numsamples_estimation//Nsteps #The number of steps taken to get "numsamples_estimation" samples (to avoid memory allocation issues)

                    samplesandprobs_final = DRNNWF.sample(numsamples=numsamples_perstep,inputdim=2)
                    energies = np.zeros((numsamples_estimation))
                    solutions = np.zeros((numsamples_estimation, N))
                    print("\nSaving energy and variance before the end of annealing")

                    for i in range(Nsteps):
                        samples_final, _ = sess.run(samplesandprobs_final)
                        energies[i*numsamples_perstep:(i+1)*numsamples_perstep] = Fullyconnected_diagonal_matrixelements(Jz,samples_final)
                        solutions[i*numsamples_perstep:(i+1)*numsamples_perstep] = samples_final
                        print("Sampling step:" , i+1, "/", Nsteps)
                    print("meanE = ", np.mean(energies))
                    print("varE = ", np.var(energies))
                    print("minE = ",np.min(energies))
                    print("Elapsed time is =", time.time()-start, " seconds")
                    return np.mean(energies), np.min(energies)

                # Run gradient descent step
                sess.run(optstep,feed_dict={Eloc:local_energies, sampleplaceholder_forgrad: samples, learningrate_placeholder: lr, T_placeholder:T})

                if it%5 == 0:
                    print("Elapsed time is =", time.time()-start, " seconds")
                    print('\n\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_instance", type=str,
                        help="input the data file for the problem instance")
    args = parser.parse_args()

    path = args.problem_instance
    seed = 0
    vca_config = config(path, seed)
    mean_energies, min_energies = vca_solver(vca_config)