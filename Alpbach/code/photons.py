from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

lam = 2.5e-6  # m
delta_lam = 1e-8  # Band width (m)
delta_lam = lam/200
line_depth = 1#0.02
radius_of_earth = 6.37e6
radius_of_planet = radius_of_earth  # m
planet_distance_parsec = 50
area_of_telescope = pi*2**2  # m^2
steradian_in_a_sphere = 4*pi

# T = 3600
T = 5772  # K

kB = 1.38e-23  #m^2 kg s^-2 K^-1
c = 3e8  # m s^-2
h = 6.626e-34  # kg m^2 s^-1
sun_surface_area = 4*pi*7e8**2

def B(lam, T=5800):  # W sr^-1 m^-2 s^-1
    return 2*h*c**2/lam**5 * 1.0/(np.exp(h*c/(lam*kB*T)) - 1)
wavelengths = np.logspace(-8, -2, 100000)
star_tot_flux = np.sum(B(wavelengths, T)[1:]*(wavelengths[1:]-wavelengths[:-1]))
print("Total star flux: ", star_tot_flux*sun_surface_area*steradian_in_a_sphere)

nu = c/lam  # Frequency

energy_per_photon = h*nu

sun_energy_at_wavelength = B(lam, T)*sun_surface_area*steradian_in_a_sphere*delta_lam
print("Star power at channel (W):", sun_energy_at_wavelength)

photons_per_s = sun_energy_at_wavelength/energy_per_photon
print("Photons/s at channel:", photons_per_s)

parsec_to_meter = 3.086e+16
area_telescope_sphere = 4*pi*(planet_distance_parsec*parsec_to_meter)**2
print("Telescope megasurface fraction:", area_of_telescope/area_telescope_sphere)

photons_hitting_telescope_per_s = photons_per_s*area_of_telescope/area_telescope_sphere
photons_hitting_telescope_per_h = 3600*photons_per_s*area_of_telescope/area_telescope_sphere
print(f"Photons hitting telescope / s: {photons_hitting_telescope_per_s:e}")
print(f"Photons hitting telescope / h: {photons_hitting_telescope_per_h:e}")

# au_to_meter = 1.5e11
area_of_earth = pi*radius_of_planet**2

planet_area_fraction = area_of_earth/sun_surface_area
atmosphere_area_fraction = planet_area_fraction/50#/300
print("Atmosphere/sun area fraction: ", atmosphere_area_fraction)

photons_per_s_rms = np.sqrt(photons_hitting_telescope_per_s)
photons_atmosphere_per_s = line_depth*atmosphere_area_fraction*photons_hitting_telescope_per_s

photons_atmosphere_per_h = photons_atmosphere_per_s*3600
photons_hitting_telescope_per_h = photons_hitting_telescope_per_s*3600
photons_per_h_rms = np.sqrt(photons_hitting_telescope_per_h)

print(f"{photons_atmosphere_per_s:e}, {photons_per_s_rms:e}")
print(f"Photons absorbed / hour: {photons_atmosphere_per_h:e}")
print(f"Photon rms / hour: {photons_per_h_rms:e}")
print(f"S/N per hour: {photons_atmosphere_per_h/photons_per_h_rms}")
print(f"Hour for S/N = 5: {(5.0/(photons_atmosphere_per_h/photons_per_h_rms))**2}")

hours = 100
print(f"ppm for observation of star: {1e6/np.sqrt(hours*photons_hitting_telescope_per_h)}")
