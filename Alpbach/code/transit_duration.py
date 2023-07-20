from math import pi, sqrt
import numpy as np

def transit(period, R_star, R_planet, a):
    return period/pi * np.arcsin(R_star/a*sqrt(1 + (R_planet/R_star)**2))


au2meter = 1.5e+11

R_star = 7e8
a = au2meter
R_planet = 6e6
period = 365*3600*24

print(transit(period, R_star, R_planet, a))