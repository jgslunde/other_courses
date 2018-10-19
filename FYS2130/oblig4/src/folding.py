import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
dt = 1.0/Fs
N = 1024
t = np.linspace(0, N*dt, N)

for freq in [100,200,400,700,950,1300]:
    x = 0.8 * np.cos(2*np.pi*freq*t)
    X = np.fft.fft(x,N)/N

    plt.plot(t, x)
    plt.title("Time spectrum of %dHz oscilation" % freq)
    plt.xlabel("Time[S]")
    plt.ylabel("Amplitude")
    plt.savefig("../fig/timespec%d.pdf" % freq)
    plt.clf()

    frekv = (Fs/2)*np.linspace(0,1,N/2)
    plt.plot(frekv, 2*np.abs(X[:N/2]))
    plt.title("Frequency spectrum of %dHz oscilation" % freq)
    plt.xlabel("Frequency[Hz]")
    plt.ylabel("Amplitude")
    plt.savefig("../fig/freqspec%d.pdf" % freq)
    plt.clf()
