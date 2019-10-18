import numpy as np
import matplotlib.pyplot as plt

N = 10000
x = np.linspace(-2, 2, N)
R = 0.5

W = np.where(np.abs(x) < R, 1, 0)

W = W

plt.plot(W)
plt.show()

k = np.linspace(-40, 40, 10000)

W_f = 2/k*np.sin(R*k)
Wmax = 2*R
half_idx = np.argmin(np.abs(Wmax/2 - W_f))

plt.plot(k, W_f, c="navy")
plt.axvline(x=k[half_idx], ls="--", c="crimson")
plt.axvline(x=-k[half_idx], ls="--", c="crimson")
plt.axhline(y=Wmax/2, ls="--", c="crimson")
plt.savefig("tophat.png")

