# Shows the effect of Lowpass and Highpass filters made from an RC circuit.

import numpy as np
import matplotlib.pyplot as plt


C = 0.01    # Capacitance
R = 0.02    # Resistance
Vs = 1000      # Voltage Source
freq = np.linspace(1,1e6,1e5)   # Frequencies from 1 to 10^6 Hz


def V_lowpass(freq):
    # Returns amplitide of given frequencies passed through a lowpass filter
    Xc = 1 / (2*np.pi*C*freq)
    return Xc / np.sqrt(Xc**2 + R**2) * Vs

def V_hightpass(freq):
    # Returns amplitide of given frequencies passed through a highpass filter
    Xc = 1 / (2*np.pi*C*freq)
    return R / np.sqrt(Xc**2 + R**2) * Vs

def f_c():
    # The "crossing point" frequency, where High- and Lowpass filters returns the same amplitude.
    # Has value 1/sqrt(2) of the maximum amplitude, which is Vs.
    return 1 / (2*np.pi*R*C)


V_lowpass_values = V_lowpass(freq)
V_highpass_values = V_hightpass(freq)


plt.loglog( freq, V_lowpass_values, label = "Lowpass")
plt.loglog( freq, V_highpass_values, label = "Highpass" )
plt.axvline( x=f_c(), color = "r", label = "f_c" )
plt.axvline( x=20, color = "k", ls = "--", label = "Human hearing range")
plt.axvline( x=20000, color = "k", ls = "--")
plt.xlabel("Frequency (log)")
plt.ylabel("Amplitude (log)")
plt.legend(loc = 4)
plt.savefig("filters.pdf")
plt.show()
