import numpy as np
import matplotlib.pyplot as plt

N = 2**14
Fs = 1024
dt = 1.0/Fs
periods = 16
omega = 2*np.pi*13 * Fs / float(N)
t = np.linspace(0, N*dt, N)

ones = np.ones(N/32)
x = np.zeros(N)

for i in range(0,32,2):
    x[i*N/32:(i+1)*N/32] = ones

plt.plot(t, x)
plt.axis([0,17,0,1.2])
plt.title("Time spectrum of square function")
plt.xlabel("Time[S]")
plt.ylabel("Amplitude")
plt.savefig("../fig/squaretimespec.pdf")
plt.clf()

X = np.fft.fft(x,N)/N
frekv  = (Fs/2)*np.linspace(0,1,N/2)

plt.plot(frekv, 2*np.abs(X[:N/2]))
plt.title("Frequency spectrum of square function")
plt.xlabel("Frequency[Hz]")
plt.ylabel("Amplitude")
plt.savefig("../fig/squarefreqspec1.pdf")
plt.clf()

plt.plot(frekv, 2*np.abs(X[:N/2]))
plt.axis([0,10,0,1])
plt.title("Frequency spectrum of square function")
plt.xlabel("Frequency[Hz]")
plt.ylabel("Amplitude")
plt.savefig("../fig/squarefreqspec2.pdf")
