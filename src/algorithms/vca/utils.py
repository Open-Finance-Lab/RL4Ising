import tensorflow as tf
import numpy as np

def Fullyconnected_diagonal_matrixelements(Jz, samples):
    numsamples = samples.shape[0]
    N = samples.shape[1]
    energies = np.zeros((numsamples), dtype = np.float64)

    for i in range(N-1):
      values = np.expand_dims(samples[:,i], axis = -1)+samples[:,i+1:]
      valuesT = np.copy(values)
      valuesT[values==2] = +1 #If both spins are up
      valuesT[values==0] = +1 #If both spins are down
      valuesT[values==1] = -1 #If they are opposite

      energies += np.sum(valuesT*(-Jz[i,i+1:]), axis = 1)

    return energies

def Fullyconnected_localenergies(Jz, Bx, samples, queue_samples, log_probs_tensor, samples_placeholder, log_probs, sess):
    numsamples = samples.shape[0]
    N = samples.shape[1]
    
    local_energies = np.zeros((numsamples), dtype = np.float64)

    for i in range(N-1):
      # for j in range(i+1,N):
      values = np.expand_dims(samples[:,i], axis = -1)+samples[:,i+1:]
      valuesT = np.copy(values)
      valuesT[values==2] = +1 #If both spins are up
      valuesT[values==0] = +1 #If both spins are down
      valuesT[values==1] = -1 #If they are opposite

      local_energies += np.sum(valuesT*(-Jz[i,i+1:]), axis = 1)

    queue_samples[0] = samples #storing the diagonal samples

    if Bx != 0:
        count = 0
        for i in range(N-1):  #Non-diagonal elements
            valuesT = np.copy(samples)
            valuesT[:,i][samples[:,i]==1] = 0 #Flip spin i
            valuesT[:,i][samples[:,i]==0] = 1 #Flip spin i

            count += 1
            queue_samples[count] = valuesT

        len_sigmas = (N+1)*numsamples
        steps = len_sigmas//50000+1 #I want a maximum of 50000 in batch size just to be safe I don't allocate too much memory

        queue_samples_reshaped = np.reshape(queue_samples, [(N+1)*numsamples, N])
        for i in range(steps):
          if i < steps-1:
              cut = slice((i*len_sigmas)//steps,((i+1)*len_sigmas)//steps)
          else:
              cut = slice((i*len_sigmas)//steps,len_sigmas)
          log_probs[cut] = sess.run(log_probs_tensor, feed_dict={samples_placeholder:queue_samples_reshaped[cut]})


        log_probs_reshaped = np.reshape(log_probs, [N+1,numsamples])
        for j in range(numsamples):
            local_energies[j] += -Bx*np.sum(0.5*(np.exp(log_probs_reshaped[1:,j]-log_probs_reshaped[0,j])))

    return local_energies