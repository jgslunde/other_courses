import matplotlib.pyplot as plt
from numpy import linspace, exp

def z(j, theta, T):
    return (2*j + 1)*exp(-j*(j+1)*theta/T)

j = linspace(0, 100, 100)

plt.plot(j, z(j, 1, 1000), 'bo')
plt.title("$z(j)$ for $\\theta_r = 1$, $T = 1000$")
plt.ylabel("Partition function weight of j'th energy level")
plt.xlabel("Energy level j")
plt.savefig("taske_1.pdf")
plt.clf()
plt.plot(j, z(j, 1, 10), 'bo')
plt.title("$z(j)$ for $\\theta_r = 1$, $T = 10$")
plt.ylabel("Partition function weight of j'th energy level")
plt.xlabel("Energy level j")
plt.savefig("taske_2.pdf")
plt.clf()
plt.plot(j, z(j, 1000, 1), 'bo')
plt.title("$z(j)$ for $\\theta_r = 1000$, $T = 1$")
plt.ylabel("Partition function weight of j'th energy level")
plt.xlabel("Energy level j")
plt.savefig("taske_3.pdf")
