import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

M = 100000
deltas = []

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

    if not (delta_array > 1).any():
        deltas.append(delta_array[-1])

deltas = np.array(deltas)

def Pnc(delta):
    var = np.pi
    return 1/np.sqrt(2*np.pi*var)*(np.exp(-delta**2/(2*var)) - np.exp(-(2*1-delta)**2/(2*var)))

plt.hist(deltas, bins="auto", density="true")
plt.plot(np.sort(deltas), Pnc(np.sort(deltas)))
plt.savefig("hist2.png")