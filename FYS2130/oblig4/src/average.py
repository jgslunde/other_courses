import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
dt = 1.0/Fs
N = 1024
X = 0

t = np.linspace(0, N*dt, N)
x = 1.2*np.sin(2*t) + 0.4*np.cos(10*t)

X = np.fft.fft(x,N)/N

average = np.sum(x)/N
plt.plot(t, x, label="$x_n$")
plt.axhline(y=np.abs(X[0]), color="r", ls=":", label="$X_0$")
plt.axhline(y=average, color="k", ls="--", label="average")
plt.legend()
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axis([0,1,0,1.8])
plt.title("Comparing first step in fourier-transformation to original signal")
plt.savefig("../fig/average.pdf")
plt.show()
