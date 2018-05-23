import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

L = 1.243
N = 14

omega = np.array([119.4, 118.1, 118.1, 117.9, 117.9, 117.9, 117.8, 117.8, 117.8, 117.7, 117.6, 117.6, 117.5, 117.6])*1e-2
average_omega = (np.sum(omega)/N)

f = np.array([554, 682, 793, 905, 1017, 1130, 1242, 1355, 1468, 1581, 1694, 1807, 1920, 2033])
n = np.arange(0,N)

avg_omega = 115.6
f = np.array([671, 781, 891, 1002, 1113, 1224, 1335, 1445, 1558, 1669, 1779, 1890])
N = len(f)
n = np.arange(0,N)
slope, intercept, r, p, std_err = linregress(n, f)
print(f[:-1]-f[1:])
plt.plot(n, f, "ro")
plt.plot([0,N], [intercept, intercept+slope*14])
# plt.show()

print(slope)

c_co2 = slope*2*L
print(c_co2)




f = 5
R = 8.31  # J/K
M_mol = 44*1e-3  # kg
T = 25 - np.log(average_omega)*24 + 273.15  # K
print(T)
co2 = (np.sqrt((f+2)*R*T/(f*M_mol)))
print(co2)
print(std_err/co2, r, p)
