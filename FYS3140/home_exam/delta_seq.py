import numpy as np
import matplotlib.pyplot as plt

def phi(x, n):
    return n/np.pi * 1/(1+n**2*x**2)

max_N = 40

t_1 = np.linspace(-4,4, int(1e6))
a = 2
phi_f_1 = 1/(2*a)*phi(t_1-a, max_N) + 1/(2*a)*phi(t_1+a, max_N)
plt.plot(t_1, phi_f_1, label="$\phi_n(t^2-a^2)$, $a=2$")
plt.axvline(x=a, ls="--", c="r")
plt.axvline(x=-a, ls="--", c="r")
plt.xlabel("t")
plt.legend()
plt.title("Delta sequence plot of $(t^2-a^2)$ with $n=40$")
plt.savefig("delta_seq_a.pdf")
plt.clf()

t_2 = np.linspace(-7,7, int(1e6))
phi_f_2 = 0
for i in range(-7,7):
    phi_f_2 += phi(t_2-np.pi*i, max_N)
plt.plot(t_2, phi_f_2, label="$\phi_n(\sin(t))$")
for i in range(-2,3):
    plt.axvline(x=np.pi*i, ls="--", c="r")
plt.xlabel("t")
plt.title("Delta sequence plot of $(sin(t))$ with $n=40$")
plt.legend()
plt.savefig("delta_seq_sin.pdf")
plt.clf()