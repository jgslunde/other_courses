import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 1000)
plt.plot(t, np.cos(t), c='r', label=r"$E(t)$")
plt.plot(t, np.cos(t), c='b', ls = ':', label=r"$j(t), \omega \tau \ll 1$")
plt.plot(t, np.sin(t), c='g', label=r"$j(t), \omega \tau \gg 1$")
plt.xlabel(r"$t/\omega$")
plt.ylabel(r"E | j")
plt.legend()
plt.savefig("asdf2.pdf")