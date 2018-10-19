from __future__ import division
from numpy import sin, cos, exp, pi, log, linspace, logspace, log10
import numpy as np
import matplotlib.pyplot as plt

N = 8192  # Nr of time-points
f1 = 1000.0  # Hz
f2 = 1600.0  # Hz
fs = 10000.0  # Sampling freq, Hz
c1 = 1.0
c2 = 1.7

#__Exercise a__
time_points = linspace(0, (N-1)/float(fs), int(N))

def function(t):
    return c1*sin(2*pi*f1*t) + c2*cos(2*pi*f2*t)

f_array = function(time_points)
plt.plot(time_points, f_array)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Time domain of sinuswave')
plt.savefig('fig/sinus_wave1.pdf')
plt.clf()
plt.plot(time_points[0:128], f_array[0:128])
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Time domain of sinuswave')
plt.savefig('fig/sinus_wave2.pdf')
plt.clf()


#__ Exercise b__
FT_signal = np.fft.fft(f_array, N)/N
freq = np.fft.fftfreq(N, d=1/fs)
plt.axis([0,2000,0,1.7])
plt.plot(freq[:int(N/2)], 2*np.abs(FT_signal[:int(N/2)]))
plt.xlabel('Frequency [Hertz]')
plt.ylabel('Fourier coefficient (Relative amplitude)')
plt.title('Frequency domain of sinus wave')
plt.savefig('fig/FT_sinus_wave.pdf')
plt.clf()


#__Exercise c__
def FT_wavelet(w, wa, K):  # Analytical FT of wavelet
    return 2*(exp(-(K*(w-wa)/wa)**2) -exp(-K**2)*exp(-(K*w/wa)**2))

def WL_solver(FT_func, fs, K, M, f_start, f_stop, savename = None):
    WL_matrix = np.zeros(shape=(M,N))  # TimePoints X FrequencyPoints
    f = np.linspace(0, fs*(N-1.0)/N, N)
    analyzing_freq = logspace(log10(f_start), log10(f_stop), M)

    for i in xrange(M):
        FT_wl = FT_wavelet(f, analyzing_freq[i], K)
        WL_matrix[i,:] = np.sqrt(np.abs(np.fft.ifft(FT_wl*FT_func)))

    plt.pcolormesh(time_points, analyzing_freq, WL_matrix)
    plt.xlabel('Time [seconds]')
    plt.ylabel('Frequency [Hertz]')
    plt.title('Wavelet transformation of wave for K = %d' % K)
    plt.colorbar()
    if savename == None:
        plt.show()
    else:
        plt.savefig('fig/' + savename + '.png')
        plt.clf()

K1 = 24
K2 = 200
f_start = 800.0
f_stop = 2000.0
M = 1000

WL_solver(FT_signal, fs, K1, M, f_start, f_stop, savename = 'wavelet_sinus_k=24')
WL_solver(FT_signal, fs, K2, M, f_start, f_stop, savename = 'wavelet_sinus_k=200')


#__Exercise d__
K3 = 100
t1 = 0.15
t2 = 0.5
sigma1 = 0.01
sigma2 = 0.1

def function2(t):
    return c1*sin(2*pi*f1*t)*exp(-((t-t1)/sigma1)**2) + c2*cos(2*pi*f2*t)*exp(-((t-t2)/sigma2)**2)

f_array2 = function2(time_points)
plt.plot(time_points, f_array2)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Time domain of gaussian waves')
plt.savefig('fig/gaussian_wave.pdf')
plt.clf()

FT_signal2 = np.fft.fft(f_array2, N)/N
freq = np.fft.fftfreq(N, d=1/fs)
plt.axis([0,2000,0,0.5])
plt.plot(freq[:int(N/2)], 2*np.abs(FT_signal2[:int(N/2)]))
plt.xlabel('Frequency [Hertz]')
plt.ylabel('Fourier coefficient (Relative amplitude)')
plt.title('Frequency domain of gaussian waves')
plt.savefig('fig/FT_gaussian_wave.pdf')
plt.clf()

WL_solver(FT_signal2, fs, K1, M, f_start, f_stop, savename = 'wavelet_gaussian_k=24')
WL_solver(FT_signal2, fs, K3, M, f_start, f_stop, savename = 'wavelet_gaussian_k=100')
