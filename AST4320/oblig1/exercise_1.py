import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def H_func(O_m, O_r, O_d, a):
    return np.sqrt(O_m/a**3 + O_r/a**4 + O_d)

def diffeq(x, a, O_m, O_r, O_d):
    # O_m, O_r, O_d = p
    x1, x2 = x
    
    H = H_func(O_m, O_r, O_d, a)

    x1_der = x2/(a*H)
    x2_der = -2*x2/a + 3.0/2*x1/a*H

    return [x1_der, x2_der]


delta_list = []
a_list = []

for O_list in [[1.0, 0.0, 0.0], [0.3, 0.0, 0.7], [0.8, 0.0, 0.2]]:

    a0 = 10**-3
    x10 = 10**-3
    x20 = H_func(*O_list, a0)*a0
    a = np.logspace(-3, 0, 10001)

    initial_cond = [x10, x20]

    x1, x2 = odeint(diffeq, initial_cond, a, (O_list[0], O_list[1], O_list[2])).T

    a_list.append(a)
    delta_list.append(x1)
    plt.loglog(a, x1)

plt.show()


for i in range(3):
    loga = np.log(a_list[i])
    logdelta = np.log(delta_list[i])

    f = np.zeros(len(x1)-1)
    for i in range(len(f)):
        f[i] = (logdelta[i+1] - logdelta[i])/(loga[i+1] - loga[i])

    z = 1/a - 1
    plt.plot(z[1:], f)
plt.show()