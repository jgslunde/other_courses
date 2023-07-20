from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

lam = 20e-6  # m
delta_lam = 1e-8  # Band width (m)
line_depth = 1#0.02
radius_of_earth = 6.37e6
radius_of_planet = radius_of_earth  # m
planet_surface_area = 4*pi*radius_of_planet
planet_distance_parsec = 10
area_of_telescope = pi*2**2  # m^2
steradian_in_a_sphere = 4*pi

kB = 1.38e-23  #m^2 kg s^-2 K^-1
c = 3e8  # m s^-2
h = 6.626e-34  # kg m^2 s^-1
sun_surface_area = 4*pi*7e8**2

def B(lam, T=5800):  # W sr^-1 m^-2 s
    return 2*h*c**2/lam**5 * 1.0/(np.exp(h*c/(lam*kB*T)) - 1)
wavelengths = np.logspace(-8, 0, 100000)

print(B(20e-6, 5800)/B(20e-6, 300))

# wavelengths = np.logspace(-6, -4, 10000)
# plt.loglog(wavelengths, B(wavelengths, 5800))
# plt.loglog(wavelengths, B(wavelengths, 300))
# plt.show()

# plt.loglog(wavelengths, B(wavelengths, 5800)/B(wavelengths, 300))
# plt.ylim(1, 1e5)
# plt.show()


T_star = 5800  # K
T_planet = 300  # K
nu = c/lam  # Frequency

energy_per_photon = h*nu

sun_energy_at_wavelength = B(lam, T_star)*sun_surface_area*steradian_in_a_sphere*delta_lam
print(f"Star surface area: (m^2): {sun_surface_area:e}")
print(f"Star power at channel (W): {sun_energy_at_wavelength:e}")

planet_energy_at_wavelength = B(lam, T_planet)*planet_surface_area*steradian_in_a_sphere*delta_lam
print(f"Planet surface area: (m^2): {planet_surface_area:e}")
print(f"Planet power at channel (W): {planet_energy_at_wavelength:e}")

photons_per_s_star = sun_energy_at_wavelength/energy_per_photon
photons_per_s = planet_energy_at_wavelength/energy_per_photon
print(f"Photons/s at channel from star: {photons_per_s_star:e}")
print(f"Photons/s at channel from planet: {photons_per_s:e}")

parsec_to_meter = 3.086e+16
area_telescope_sphere = 4*pi*(planet_distance_parsec*parsec_to_meter)**2
print("Telescope megasurface fraction:", area_of_telescope/area_telescope_sphere)

photons_hitting_telescope_per_s = photons_per_s*area_of_telescope/area_telescope_sphere
photons_hitting_telescope_per_h = 3600*photons_per_s*area_of_telescope/area_telescope_sphere
print(f"Photons hitting telescope / s: {photons_hitting_telescope_per_s:e}")
# print(f"Photons hitting telescope / h: {photons_hitting_telescope_per_h:e}")
photons_hitting_telescope_per_s_star = photons_per_s_star*area_of_telescope/area_telescope_sphere
photons_hitting_telescope_per_h_star = 3600*photons_per_s_star*area_of_telescope/area_telescope_sphere
print(f"Star photons hitting telescope / s: {photons_hitting_telescope_per_s_star:e}")

# au_to_meter = 1.5e11
area_of_earth = pi*radius_of_planet**2

photons_per_s_rms = np.sqrt(photons_hitting_telescope_per_s_star)
photons_per_h_rms = np.sqrt(photons_hitting_telescope_per_h_star)
photons_from_planet_per_s = line_depth*photons_hitting_telescope_per_s

photons_from_planet_per_h = photons_from_planet_per_s*3600
photons_hitting_telescope_per_h = photons_hitting_telescope_per_s*3600

print(f"{photons_from_planet_per_s:e}, {photons_per_s_rms:e}")
print(f"Photons absorbed / hour: {photons_from_planet_per_h:e}")
print(f"Photon rms / hour: {photons_per_h_rms:e}")
print(f"S/N per hour: {photons_from_planet_per_h/photons_per_h_rms}")
print(f"Hour for S/N = 5: {(5.0/(photons_from_planet_per_h/photons_per_h_rms))**2}")
