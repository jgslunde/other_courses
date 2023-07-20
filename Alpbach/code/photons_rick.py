import numpy as np
import scipy as scp
import pandas as pd
import matplotlib.pyplot as plt
lightspeed = 299792458
# Solar Flux in Watts
F_sun = 3.8 * 10 ** 26
# Radius Sun
R_sun = 6.957 * 10 ** 8
# Radius of Earth in meters
R_E = 6.371 * 10 ** 6
g_E = 9.81
F_E = 2.5 * 10 ** 17
# MIR energy in Joules
E_y = 1.1 * 10 ** (-20)
# Stefan-Boltzmann constant
sigma = 5.670374419 * 10 ** (-8)
# Planck constant
h = 6.62607015 * 10 ** (-34)
# Boltzmann constant
kb = 1.380649 * 10 ** (-23)
# Gas constant
R = 8.31446261815324
mu_atmo = 2.3 #g / mol
def BBR(lam, T):
    """
    Calculates the black body radiation
    :param T: Temperature in Kelvin
    :param lam: Wavelength in micrometers
    :return: Black body radiation
    """
    lam = lam * 10 ** (-6)
    BBR1 = 2 * h * lightspeed ** 2 / lam ** 5
    BBR2 = 1 / (np.exp(h * lightspeed / (lam * kb * T)) - 1)
    BBR = BBR1 * BBR2
    return BBR * 10 ** (-6)
def integral_BBR(T, lam_min, lam_max):
    """
    Calculates the integral of the black body radiation
    :param T: Temperature in Kelvin
    :param lam_min: lambda min in micrometers
    :param lam_max: lambda max in micrometers
    :return: Integral of the black body radiation
    """
    # Pi multiplication because of angle of emission based on Wikipedia article
    integral = np.pi * scp.integrate.quad(BBR, lam_min, lam_max, args=T)[0]
    return integral
def SNR_eclipse(F_s, t_eclipse, N, lam_min, lam_max, d, A_inst, T_p, Rp, R_spec, Ab=0.2):
    """
    Calculates the SNR for a eclipse observation
    :param F_s: Flux of star in Watts
    :param t_eclipse: eclipse time in seconds
    :param N: Number of eclipses
    :param lam_min: lambda min in micrometers
    :param lam_max: lambda max in micrometers
    :param d: distance to star in meters
    :param D: Diameter of telescope in meters
    :param T_p: Temperature of planet in Kelvin
    :param Rp: Radius of planet in meters
    :param Ab: Bond albedo of planet
    :return: SNR signal-to-noise ratio
    """
    signal = (1 - Ab) * integral_BBR(T_p, lam_min, lam_max) * Rp ** 2 * A_inst / (R_spec * E_y * d ** 2)
    noise_signal = signal
    noise_star = N_photons_star(F_s, lam_min, lam_max, d, A_inst, R_spec)
    noise = np.sqrt(noise_signal ** 2 + noise_star ** 2)
    SNR = np.sqrt(t_eclipse) * N * signal / noise
    return SNR, 100*(noise ** 2 / noise_signal ** 2), 100*(noise ** 2 / noise_star ** 2)
def N_photons_star(F_s, lam_min, lam_max, d, A_inst, R_spec):
    """
    Calculates the number of photons from the star
    :param F_s: Flux of star in Watts
    :param lam_min: lambda min in micrometers
    :param lam_max: lambda max in micrometers
    :param d: distance to star in meters
    :param D: Diameter of telescope in meters
    :return: Number of photons
    """
    N_photons = F_s * A_inst / (4 * np.pi * d ** 2 * E_y * R_spec)
    return N_photons
def SNR_transit(F_s, t_transit, N, lam_min, lam_max, d, A_inst, precision, Rp, Ab=0.2):
    """
    Calculates the SNR for a transit observation
    :param F_s: Flux of star in Watts
    :param t_transit: transit time in seconds
    :param N: Number of transits
    :param lam_min: lambda min in micrometers
    :param lam_max: lambda max in micrometers
    :param d: distance to star in meters
    :param D: Diameter of telescope in meters
    :param precision: precision of telescope
    :param Ab: Bond albedo of planet
    :return: SNR signal to noise ratio
    """
    stellar_photons = N_photons_star(F_s, lam_min, lam_max, d, A_inst, R_spec)
    print(stellar_photons)
    signal_transmission = precision * stellar_photons
    signal_thermal = (1-Ab) * integral_BBR(T_p, lam_min, lam_max) * Rp ** 2 * A_inst / (R_spec * E_y * d ** 2)
    signal = signal_thermal + signal_transmission
    noise_signal = np.sqrt(stellar_photons)
    noise = noise_signal
    SNR = N * np.sqrt(t_transit) * signal / noise
    print("signal:", signal_transmission, signal_thermal)
    print("noise:", noise)
    return SNR, 100*(noise ** 2 / noise_signal ** 2)
def dream_precision(R_p, atmosphere, R_s, T_p):
    """
    Calculates the precision of the DREAMS instrument
    :param R_p: Radius of planet in meters
    :param atmosphere: atmospheric height in meters
    :param R_s: Radius of star in meters
    :param R_spec: Spectral Resolution of telescope
    :return: precision
    """
    g_p = (R_p / R_E) ** 3 * g_E
    scale_height = 1000 * R * T_p / (mu_atmo * g_p)
    precision = (R_p / R_s)**2 * (scale_height / R_p)
    return precision
# Star Specs
star_selection = pd.DataFrame({'stype': ['M5', 'M4', 'M3', 'M2', 'M1', 'M0',
                                         'K7', 'K5', 'K4', 'K3', 'K2', 'K1', 'K0',
                                         'G8', 'G5', 'G2', 'G1', 'G0',
                                         'F8', 'F7', 'F6', 'F5', 'F3', 'F2', 'F0'],
                               'Ts': [3200, 3400, 3500, 3600, 3700, 3750,
                                      4000, 4400, 4600, 4800, 4960, 5110, 5240,
                                      5440, 5660, 5800, 5930, 6050,
                                      6300, 6400, 6550, 6700, 6850, 7050, 7350],
                               'Rs': [0.27, 0.34, 0.41, 0.48, 0.55, 0.60,
                                      0.66, 0.72, 0.75, 0.78, 0.81, 0.84, 0.85,
                                      0.88, 0.92, 1.0, 1.05, 1.1,
                                      1.15, 1.2, 1.25, 1.3, 1.36, 1.43, 1.5],
                               })
lam_min = 2.5
lam_max = 21
T_s = 5777
pc = 3 * 10 ** 16
d = 10 * pc
R_s = R_sun
integral_s = integral_BBR(T_s, lam_min, lam_max)
F_s = integral_s * 4 * np.pi * R_s ** 2
# Planet Specs
T_p = 300
R_p = 1 * R_E
atmo_height = R_p / 500
t_transit = 5 * 60 * 60
integral_p = integral_BBR(T_p, 2.5, 21)
# Instrument Specs
N_transit = 10
D = 4
R_spec = 350
A_inst = np.pi * (D / 2) ** 2
precision_dream = dream_precision(R_p, atmo_height, R_s, T_p)
print(precision_dream)
SNR_trans, noise_signal_trans = SNR_transit(F_s, t_transit, N_transit, lam_min, lam_max, d, A_inst, precision_dream, R_p)
SNR_ecl, noise_signal_ecl, noise_star_ecl = SNR_eclipse(F_s, t_transit, 2 * N_transit, lam_min, lam_max, d, A_inst, T_p,
                                                        R_p, R_spec)
SB_naive = sigma * T_p ** 4
print("Non-naive to Naive difference planet Flux:", integral_p, SB_naive)
print("Non-naive to Naive difference stellar Flux:", F_s,
      integral_BBR(T_s, 0, np.inf) * 4 * np.pi * R_s ** 2)
print("Transit SNR:", SNR_trans, precision_dream)
print("Eclipse SNR:", SNR_ecl)
"""
F_star, precision_t, SNRt, noise_sig_t, SNRe, noise_sig_e, noise_star_e = [], [], [], [], [], [], []
for i, T in enumerate(star_selection['Ts']):
    integral_dummy = integral_BBR(T, lam_min, lam_max)
    F_dummy = integral_dummy * 4 * np.pi * (R_sun*star_selection['Rs'][i]) ** 2
    F_star.append(F_dummy)
    precision_dummy = dream_precision(R_p, atmo_height, (R_sun * star_selection['Rs'][i]), R_spec)
    precision_t.append(precision_dummy)
    SNRt_dummy, noise_sig_t_dummy = SNR_transit(F_dummy, t_transit, N_transit, lam_min, lam_max, d, A_inst, precision_dummy)
    SNRt.append(SNRt_dummy)
    noise_sig_t.append(noise_sig_t_dummy)
    SNRe_dummy, noise_sig_e_dummy, noise_star_e_dummy = SNR_eclipse(F_dummy, t_transit, 2 * N_transit, lam_min, lam_max, d, A_inst, T_p,
                                                  R_p, R_spec)
    SNRe.append(SNRe_dummy)
    noise_sig_e.append(noise_sig_e_dummy)
    noise_star_e.append(noise_star_e_dummy)
results = pd.DataFrame({'stype': star_selection['stype'],
                        'Ts': star_selection['Ts'],
                        'Rs': star_selection['Rs'],
                        'F_star': F_star,
                        'SNRt': SNRt,
                        'precision_t': precision_t,
                        'noise_sig_t %': noise_sig_t,
                        'SNRe': SNRe,
                        'noise_sig_e': noise_sig_e,
                        'noise_star_e': noise_star_e})
print(results.to_string())
"""