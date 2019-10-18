import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

M = 100000
deltas = np.zeros(M)

for j in trange(M):
    var = 1e-4
    Sc = (np.pi/var)**(1.0/4)
    delta = np.random.normal(0, np.sqrt(var))
    N = 101
    Sc_array = np.linspace(Sc, 1, N)
    epsilon = Sc_array[-1] - Sc_array[-2]
    delta_array = np.zeros(N)
    delta_array[0] = delta

    for i in range(1, N):
        Sc = Sc_array[i]
        var2 = (np.pi/Sc)**(1.0/4)
        beta = np.random.normal(0, np.sqrt(var2 - var))
        delta_array[i] = delta_array[i-1] + beta
        var = var2

    deltas[j] = delta_array[-1]

plt.hist(deltas, bins="auto", density="true")
plt.savefig("hist1.png")