import matplotlib.pyplot as plt
import numpy as np

def C(T, hbar=1, omega=1, kb=1):
    return (np.exp(1/T))/(T**2*(np.exp(1/T) - 1)**2)

T = np.linspace(0, 2, 1000)

plt.plot(T, C(T))
plt.ylabel("$C/3k_B$")
plt.xlabel("$k_B T / \hbar\omega$")
plt.savefig("asdf.pdf")