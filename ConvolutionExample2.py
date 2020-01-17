import numpy as np
import scipy.io.wavfile
from scipy import signal
import matplotlib.pyplot as plt


def convolution(h, x):
	result0 = np.zeros( (h.shape[0] + x.shape[0] - 1) ) 
	result1 = np.zeros( (h.shape[0] + x.shape[0] - 1) )
	n = h.shape[0]
	end = len(x)
	for k in range(0, n):
		result0[k:(k+end)] += h[k, 0] * x[:, 0]
		result1[k:(k+end)] += h[k, 1] * x[:, 1]

	result = np.stack( (result0, result1), axis=0 )
	result = result.T
	return result


inp_sample_rate, inp = scipy.io.wavfile.read('input.wav')
h1_sample_rate, h1 = scipy.io.wavfile.read('h1.wav')
h2_sample_rate, h2 = scipy.io.wavfile.read('h2.wav')
h3_sample_rate, h3 = scipy.io.wavfile.read('h3.wav')


y1 = convolution(1.0*h1, 1.0*inp)
y2 = convolution(1.0*h2, 1.0*inp)
y3 = convolution(1.0*h3, 1.0*inp)

y1_max = np.amax(y1)
y1 = y1 / y1_max

y2_max = np.amax(y2)
y2 = y2 / y2_max

y3_max = np.amax(y3)
y3 = y3 / y3_max

rate = inp_sample_rate

scipy.io.wavfile.write("y1.wav", rate, y1)
scipy.io.wavfile.write("y2.wav", rate, y2)
scipy.io.wavfile.write("y3.wav", rate, y3)
