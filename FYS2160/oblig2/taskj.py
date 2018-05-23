import matplotlib.pyplot as plt
from numpy import linspace, exp, arange, logspace, zeros, sum, shape

def z(j, T_theta):
    return (2*j + 1)*exp(-j*(j+1)/T_theta)


def Z(T_theta):
    if T_theta > 1e6:
        return T_theta
    else:
        j = arange(0, 1e6)
        return sum(z(j, T_theta))


T_theta_values = logspace(-1, 7, 100)
Z_values = zeros(100)
for i in range(100):
    Z_values[i] = (Z(T_theta_values[i]))

plt.loglog(T_theta_values, Z_values)
plt.xlabel("$T/\\theta_r$")
plt.ylabel("$Z_R$")
plt.savefig("taskj.pdf")

print(Z(1e6))
