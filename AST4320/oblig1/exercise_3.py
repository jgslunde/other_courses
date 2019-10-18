import numpy as np
import matplotlib.pyplot as plt

a = np.logspace(-4, 0, 1001)

def T_gas(a):
    Cg = 2.5e-3
    return Cg/a**2

def T_rad(a):
    Crad = 2.725
    return Crad/a


plt.loglog(a, T_gas(a), label="T_gas")
plt.loglog(a, T_rad(a), label="T_rad")
plt.axvline(x=1/(1+1091), ls="--", c="crimson", label="Decoupling")
plt.savefig("exercise_31.png")