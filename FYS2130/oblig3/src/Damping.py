import math
import numpy as np
import matplotlib.pyplot as plt
from RungeKutta import SolveODE

# Task 4b
steps = int(1e5)
m = 0.1   # kg
k = 10   # N/m
x0 = 0.1   # m
v0 = 0   # m/s

b_critical = math.sqrt(4*m*k)   # kg/s
b_overcritical = b_critical + 10
b_undercritical = b_critical - 1.7
b_list = [b_critical, b_overcritical, b_undercritical]
b_labels = ["Critical Damping", "Overdamping", "Underdamping"]


for b, b_label in zip(b_list, b_labels):
    x, v, t = SolveODE(x0, v0, b, k, m, 4, steps)
    plt.plot(t, x, label = b_label)
plt.legend()
plt.title("Comparing damping for harmonic oscillations")
plt.xlabel("Time in seconds")
plt.ylabel("Position in meters")
plt.savefig("../fig/Damping.pdf")
plt.show()
