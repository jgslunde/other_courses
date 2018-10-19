from __future__ import division
from numpy import sin, cos, exp, pi, log, linspace, logspace, log10
import numpy as np
import matplotlib.pyplot as plt

class WaveletSolver(object):
    def __init__(self, signal_array, time_array):
        # Array of signal wave we wish to study (ampltudes).
        self.signal_array = signal_array
        # Array of corresponding time points to the signal array.
        self.time_array = time_array
        # Number of time points in signal.
        self.N = np.size(time_array)
        # Sampling frequency (time array should be linear).
        self.fs = 1/(time_array[1] - time_array[0])
        # Fourier transformation of input signal
        self.FT_signal = np.fft.fft(signal_array)

        if (self.N&(self.N-1)):
            print "N = ", self.N
            print "Consider setting N as a power of 2 for optimal performance."

    def FT_wavelet(self, f, f_mid, K):
        # Analytical solution to fourier transform of wavelet with
        # center in f_mid and wavenumber K.
        # f is a linear array of frequencies.
        return 2*(np.exp(-(K*(f-f_mid)/f_mid)**2) -np.exp(-K**2)*np.exp(-(K*f/f_mid)**2))

    def solve(self, K, M, f_start, f_stop):
        # K = Wavenumber of wavelet.
        # Higher means better precision in frequency, but lower in time.
        # f_start and f_stop = Measured frequency interval.
        # M = Number of discrete frequencies we are looking at.

        N = self.N
        fs = self.fs

        if fs < f_stop*4:
            print "Warning: Your sampling frequency (distance between two \
points in your time-array) is %.2f, which is %.2f times your chosen max frequency \
(f_stop parameter). A factor 4 is recommended. Below 2 gives corrupted results."\
% (flaot(fs), float(fs)/f_stop)

        # Wavelet matrix, (Freq x Time)
        self.WL_matrix = np.zeros(shape=(M,N))

        # Linearly spaced frequencies for each wavelet.
        freq = np.linspace(0, fs*(N-1.0)/N, N)

        # Center frequencies for wavelet. Logaritmically spaced
        # in specified interval.
        self.wavelet_mid_freqs = logspace(log10(f_start), log10(f_stop), M)

        for i in xrange(M):
            FT_wl = self.FT_wavelet(freq, self.wavelet_mid_freqs[i], K)
            self.WL_matrix[i,:] = np.sqrt(np.abs(np.fft.ifft(FT_wl*self.FT_signal)))

    def plot(self, savename = None):
        plt.pcolormesh(self.time_array, self.wavelet_mid_freqs, self.WL_matrix)
        plt.xlabel('Time [seconds]')
        plt.ylabel('Frequency [Hertz]')
        plt.title('Wavelet analysis of signal')
        plt.colorbar()
        if savename == None:
            plt.show()
        else:
            plt.savefig(savename)
            plt.clf()

    def benchmark(self, M, N):
        time_array = linspace(0,10,N)
        signal_array = sin(10*time_array)
        wavelet = WaveletSolver(signal_array, time_array)
        import time
        start_time = time.clock()
        wavelet.solve(100, M, 5, 100)
        end_time = time.clock()
        print "Time consumed = %.4f seconds" % (end_time - start_time)
