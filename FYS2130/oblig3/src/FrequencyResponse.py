import math
import numpy as np
import matplotlib.pyplot as plt
from RungeKutta import SolveODE
import os
import imageio
import sys

MakeGIF = False   # Please turn off if you don't want to create n png's and a gif.
filenames = []

# Task 4d
steps = int(1e5)
m = 0.1   # kg
k = 10   # N/m
b = 0.04   # kg/s
x0 = 0   # m
v0 = 0   # m/s
F = 0.1   # N
n = 401

def Force(t):
    return F/m * np.cos(omega_F*t)

omega_0 = math.sqrt(k/m - 0.25*b**2/m**2)

frequencies = np.linspace(0,2,n)
energies = np.zeros(n)

for i in xrange(n):
    omega_F = frequencies[i]*omega_0
    x, v, t = SolveODE(x0, v0, b, k, m, 50, steps, F = Force)

    energies[i] = 0.5*m*np.amax(x[int(0.8*steps):])**2

    if MakeGIF == True:
        plt.plot(t,x)
        plt.title("f=%.3f$f_0$" % frequencies[i])
        plt.savefig("../fig2/fig%d.png" % i)
        filenames.append("fig2/fig%d.png" % i)
        plt.clf()

    sys.stdout.write("\r %.2f percent finished" % (100*float(i)/n))
    sys.stdout.flush()

max_energy = np.amax(energies)

plt.plot(frequencies, energies, label = "$E(f)$")
plt.title("Energy of oscilating system at equilibrium \n as function of resonance frequency")
plt.xlabel("Frequencies as multiplicity of $f_0$")
plt.ylabel("Energy in Joule")
plt.axhline(y=0.5*max_energy, color = "k", linestyle = "--", label = "$0.5E_{max}$")
plt.legend()
plt.savefig("../fig/Frequency.pdf")
plt.axis([1-0.05, 1+0.05, 0.5*max_energy-0.05, 0.5*max_energy+0.05])
plt.savefig("../fig/Frequency2.pdf")

if MakeGIF == True:
    images = []
    for filename in filenames:
    	images.append(imageio.imread(filename))
    imageio.mimsave("fig2/Frequencies.gif", images)
    for filename in filenames:
        os.remove(filename)
