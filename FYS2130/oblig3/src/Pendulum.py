import math
import numpy as np
import matplotlib.pyplot as plt
from RungeKutta import SolveODE

# Task 4a
m = 0.1   # kg
k = 10   # N/m
b = 0.1   # kg/s
x0 = 0.1   # m
v0 = 0   # m/s
A = x0

gamma = 0.5*b/m
omega_0 = np.sqrt(k/m)
omega = np.sqrt(omega_0**2 - gamma**2)
omega = math.sqrt(k/m - 0.25*b**2/m**2)

def AnalyticalSolution(t):
    return A * np.cos(omega*t) * np.exp(-gamma*t)

for steps in [20, 50, 100, 1000, 10000, 100000, 1000000]:
    x, v, t = SolveODE(x0, v0, b, k, m, 10, steps)

    error_array = x - AnalyticalSolution(t)
    average_error = 100*np.linalg.norm(error_array) / steps
    largest_error = 100*np.amax(error_array)
    print "Average error for %d steps = %f cm" % (steps, average_error)
    print "Largest error for %d steps = %f cm" % (steps, largest_error)


    plt.plot(t, x, label = "Numerical Solution")
    plt.plot(t, AnalyticalSolution(t), label = "Analytical Solution")
    plt.plot(t, 0.1*np.exp(-gamma*t), label = "$e^{-\gamma t}$")
    plt.legend()
    plt.title("RK4 with %d timesteps against analytical solution" % steps)
    plt.xlabel("Time in seconds")
    plt.ylabel("Position in meters")
    plt.savefig("../fig/Pendulum%d.pdf" % steps)
    plt.show()
    plt.clf()
