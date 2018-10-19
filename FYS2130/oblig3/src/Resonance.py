import math
import numpy as np
import matplotlib.pyplot as plt
from RungeKutta import SolveODE

# Task 4c
steps = int(1e5)
m = 0.1   # kg
k = 10   # N/m
b = 0.04   # kg/s
x0 = 0   # m
v0 = 0   # m/s
F = 0.1   # N

omega_0 = math.sqrt(k/m - 0.25*b**2/m**2)
omega_F_list = [omega_0, omega_0*0.9]
omega_F_titles = ["Resonance for $\omega_F = \omega_0$", "Resonance for $\omega_F = 0.9\cdot\omega_0$"]
savenames = ["ResonanceSynced.pdf", "ResonanceUnsynced.pdf"]

def Force(t):
    if t < 20:
        return F/m * np.cos(omega_F*t)
    else:
        return 0

for (omega_F, omega_F_title, savename) in zip(omega_F_list, omega_F_titles, savenames):
    x, v, t = SolveODE(x0, v0, b, k, m, 60, steps, F = Force)
    plt.plot(t,x)
    plt.title(omega_F_title)
    plt.xlabel("Time in seconds")
    plt.ylabel("Position in meters")
    plt.savefig("../fig/" + savename)
    plt.show()
