from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt

emissivity = 0.025
T = 100
star_dist = 100  # pc
star_radius = 7e8  # m
dish_area = 4*4*pi

parsec_to_meter = 3.086e+16
b = 2.9e-3  # m K
kB = 1.38e-23  #m^2 kg s^-2 K^-1
c = 3e8  # m s^-2
h = 6.626e-34  # kg m^2 s^-1
steradian_in_a_sphere = 4*pi
star_dist_meter = star_dist*parsec_to_meter
supersphere_area = 4*pi*star_dist_meter**2
star_area = 4*pi*star_radius**2
angular_fraction = star_area/supersphere_area

def B(lam, T):  # W sr^-1 m^-2 s
    return 2*h*c**2/lam**5 * 1.0/(np.exp(h*c/(lam*kB*T)) - 1)

# print(angular_fraction)

lam = 20e-6  # m
# delta_lam = 1e-7  # m
delta_lam = lam/200 # m

B_tel = B(lam, 100)*delta_lam*dish_area

nu = c/lam  # Frequency
energy_per_photon = h*nu

photon_per_s_from_telescope_thermal = B_tel*angular_fraction/energy_per_photon

print(photon_per_s_from_telescope_thermal)


wav = np.logspace(-6, -4, 10000)
nu = c/wav
energy_per_photon = h*nu
asdf1 = B(wav, 300)*angular_fraction*delta_lam*emissivity/energy_per_photon*dish_area
asdf2 = B(wav, 100)*angular_fraction*delta_lam*emissivity/energy_per_photon*dish_area
asdf3 = B(wav, 40)*angular_fraction*delta_lam*emissivity/energy_per_photon*dish_area

plt.loglog(wav, asdf1)
plt.loglog(wav, asdf2)
plt.loglog(wav, asdf3)

plt.axvline(x=b/300)
plt.axvline(x=b/100)
plt.axvline(x=b/40)
plt.ylim(1e-4, 1e4)
plt.show()