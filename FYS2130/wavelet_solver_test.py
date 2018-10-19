from __future__ import division
from numpy import sin, cos, exp, pi, log, linspace, logspace, log10
import numpy as np
import matplotlib.pyplot as plt
from wavelet_solver import WaveletSolver

# Just parameters for the test function.
f1 = 1000.0  # Hz
f2 = 1600.0  # Hz
c1 = 1.0
c2 = 1.7
t1 = 0.15
t2 = 0.5
sigma1 = 0.01
sigma2 = 0.1
N = 8192
fs = 10000

def function(t):
    return c1*sin(2*pi*f1*t)*exp(-((t-t1)/sigma1)**2) + c2*cos(2*pi*f2*t)*exp(-((t-t2)/sigma2)**2)

time_array = np.linspace(0, (N-1.0)/fs, int(N))
signal_array = function(time_array)

# Parameters for wavelet solver.
f_start = 800.0
f_stop = 2000.0
M = 1000
K1 = 24
K2 = 200

wavelet = WaveletSolver(signal_array, time_array)
#wavelet.solve(K1, M, f_start, f_stop)
#wavelet.plot()
wavelet.benchmark(M, N)
