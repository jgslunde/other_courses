import matplotlib.pyplot as plt
from numpy import linspace, exp

T = linspace(0.1, 300, 10000)

def Cv(T, k=1.38e-23, eps=1e-21):
    return ( (3*eps**2*exp(-eps/(k*T))) / ((3*exp(-eps/(k*T)) + 1)**2*k*T**2) )

plt.plot(T, Cv(T, eps=1e-21), label="$\epsilon = 1\cdot 10^{-21}$")
plt.plot(T, Cv(T, eps=2e-21), label="$\epsilon = 2\cdot 10^{-21}$")
plt.plot(T, Cv(T, eps=4e-21), label="$\epsilon = 4\cdot 10^{-21}$")
plt.legend()
plt.xlabel("Temperature $[K]$")
plt.ylabel("Heat capacity $C_V$")
plt.savefig("taskc.pdf")
