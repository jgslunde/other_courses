from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt

lam = 1e-6  # m
delta_lam = 1e-8  # Band width (m)
line_depth = 1#0.02
radius_of_earth = 6.37e6
radius_of_planet = 3*radius_of_earth  # m
planet_distance_parsec = 10
area_of_telescope = 6*6  # m^2


kB = 1.38e-23  #m^2 kg s^-2 K^-1
c = 3e8  # m s^-2
h = 6.626e-34  # kg m^2 s^-1

def B(lam, T=5800):  # W sr^-1 m^-2 s
    return 2*h*c**2/lam**5 * 1.0/(np.exp(h*c/(lam*kB*T)) - 1)

print(B(1e-6, 300))


#plt.loglog(np.logspace(-6, -3, 1000), B(np.logspace(-8, -4, 1000), 300)/B(np.logspace(-8, -4, 1000), 5800))
#plt.ylim(1e-40, 1.0)
#plt.loglog(np.logspace(-6, -4, 1000), B(np.logspace(-6, -4, 1000), 5800))
#plt.loglog(np.logspace(-6, -4, 1000), B(np.logspace(-6, -4, 1000), 300))
plt.semilogx(np.logspace(-5, -3.5, 1000), B(np.logspace(-5, -3.5, 1000), 5800)/B(np.logspace(-5, -3.5, 1000), 300))
plt.semilogx(np.logspace(-5, -3.5, 1000), B(np.logspace(-5, -3.5, 1000), 5800)/B(np.logspace(-5, -3.5, 1000), 330))
plt.ylim(0, 2e2)
plt.show()
print(f"1 : {B(1e-6, 5800)/B(1e-6, 300)}")
print(f"2 : {B(2e-6, 5800)/B(2e-6, 300)}")
print(f"4 : {B(4e-6, 5800)/B(4e-6, 300)}")
print(f"8 : {B(8e-6, 5800)/B(8e-6, 300)}")
print(f"14 : {B(14e-6, 5800)/B(14e-6, 300)}")
print(f"20 : {B(20e-6, 5800)/B(20e-6, 300)}")