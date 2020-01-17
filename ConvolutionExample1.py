import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

def printSignal(signal):
    plt.title("Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(signal, 'ro')
    plt.show()
    return


def convolution(h, x):
    result = np.zeros( (h.shape[0] + x.shape[0] - 1) ) 
    n = h.shape[0]
    end = len(x)
    for k in range(0, n):
        result[k:(k+end)] += h[k] * x

    result = result.astype('int16')
    return result


def create_signal3():
    alpha = 1.5
    result = np.array([])
    for n in range(0,11):
        for i in range(2, n+3):
            result = np.append(result, 0)
            result[n] += np.power(alpha, i)
    for n in range(11, 14):
        for i in range(2,12):
            result = np.append(result, 0)
            result[n] += np.power(alpha, i)
    for n in range(14, 24):
        for i in range(n-11, 13):
            result = np.append(result, 0)
            result[n] += np.power(alpha, i)
    result = result * 2
    return result


t = np.arange(0, 6)

signal1 = np.array([1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1])
signal2 = np.cos( (np.pi/3) * (t) )
print(signal2)
printSignal(signal1)
printSignal(signal2)
convolved_signal = convolution(signal1, signal2)
printSignal(convolved_signal)
print("Convolution1: ")
print( convolved_signal )
print("\n\n")

signal1 = np.array([1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1])
signal2 = np.array([0,0,0,0, -1,0,1,2,3,2,1,0,-1, 0,0,0,0,0,0])
printSignal(signal1)
printSignal(signal2)
convolved_signal = convolution(signal1, signal2)
printSignal(convolved_signal)
print("Convolution2 : ")
print( convolved_signal )
print("\n\n")

signal1 = np.array( create_signal3() )
signal1[1:25] = signal1[0:24]
signal1[0] = 0
signal1 = signal1[0:25]
signal2 = np.array([-1,-2,-3,-2,-1,0,0,0,0,0,0,1,2,3,2,1,0])
printSignal(signal1)
printSignal(signal2)
convolved_signal = convolution(signal1, signal2)
printSignal(convolved_signal)
print("Convolution3 : ")
print( convolved_signal )
print("\n\n")
