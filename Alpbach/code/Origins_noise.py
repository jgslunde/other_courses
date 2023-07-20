import numpy as np
import matplotlib.pyplot as plt

sun_dist = 50  # pc
obs_time = 340  # hours

# ppm error for 340 hour of observations for the Sun at 100 pc.
point_ppm = np.array([1.8, 1.2, 4.0])
photon_ppm = np.array([0.01, 3.3, 14.0])
therm_ppm = np.array([0.5, 0.5, 0.5])
dark_ppm = np.array([2.5, 2.5, 4.0])
calib_ppm = np.array([2.0, 2.0, 10.0])
names = [
    "point_ppm",
    "photon_ppm",
    "therm_ppm",
    "dark_ppm",
    "calib_ppm",
]

factor = 100/sun_dist * np.sqrt(obs_time/340)
print(factor)
for i, x in enumerate([point_ppm, photon_ppm, therm_ppm, dark_ppm, calib_ppm]):
    print(f"{names[i]:12s}{x/factor}")

