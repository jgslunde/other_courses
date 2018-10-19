import numpy as np
import matplotlib.pyplot as plt

N = 512
Fs = 1000
dt = 1.0/Fs
periods1 = 13
periods2 = 13.2
omega1 = 2*np.pi* periods1 * Fs / float(N)
omega2 = 2*np.pi* periods2 * Fs / float(N)
t = np.linspace(0, N*dt, N)

x1 = 0.8 * np.sin(omega1*t)
x2 = 0.8 * np.sin(omega2*t)

plt.plot(t, x1, label="13 Periods")
plt.plot(t, x2, label="13.2 Periods")
plt.legend()
plt.ylabel("Amplitude")
plt.xlabel("Time[S]")
plt.title("Time spectrum of 13 and 13.2 periods of harmonic oscilations")
plt.savefig("../fig/timespec.pdf")
plt.clf()

X1 = np.fft.fft(x1,N)/N
X2 = np.fft.fft(x2,N)/N


frekv  = (Fs/2)*np.linspace(0,1,N/2)
plt.plot(frekv, 2*np.abs(X1[:N/2]), label="13 Periods")
plt.plot(frekv, 2*np.abs(X2[:N/2]), label="13.2 Periods")
plt.axis([0,50,0,1])
plt.title("Frequency spectrum of 13 and 13.2 periods of harmonic oscilations")
plt.xlabel("Frequency[Hz]")
plt.ylabel("Amplitude")
plt.legend()
plt.savefig("../fig/freqspec.pdf")
