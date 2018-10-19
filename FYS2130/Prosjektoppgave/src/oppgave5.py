import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

N = 200  # Number of strings between mass-points.
dt = 0.01
m = 0.02  # Mass of each mass-point. Constant in this run.
k = 10.0  # Spring constant.
i = np.array(range(N))
lamb = 199/3.5
freq = 1/lamb*np.sqrt(k/m)
time_steps = int(10/(freq*dt))

def y_init_cond(i):
    # Initial Conditions of string at t=0.
    return np.sin(7*i*np.pi/(N-1))

y_min = y_init_cond(i)
y_0 = y_init_cond(i)
y_plus = np.zeros(N)
y_time = np.zeros(time_steps)

beta = k*dt**2/m  # Can initialize beta outside loop because of constant mass.

for t in range(time_steps):
    y_plus[1:-1] = beta*(-2*y_0[1:-1] + y_0[:-2] + y_0[2:]) + 2*y_0[1:-1] - y_min[1:-1]
    y_min[:] = y_0
    y_0[:] = y_plus
    y_time[t] = y_0[99]

timepoints = np.linspace(0, time_steps*dt, time_steps)
plt.axis([0,timepoints[-1], -1.2, 1.2])
plt.title('Oscilation of the 100th point over time')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude [meters]')
plt.plot(timepoints, y_time, label = '$y_{99}(t)$')
plt.legend(loc = 1)
plt.savefig('../fig/100_point_oscilation.pdf')
plt.clf()

# Calcualting frequency numerically:
local_maxima = argrelextrema(y_time, np.greater)[0]  # Finds local maxima
maxima_distance = local_maxima[1:] - local_maxima[:-1]
numerical_periods = maxima_distance*dt
numerical_frequencies = 1/numerical_periods
average_numerical_frequency = np.sum(numerical_frequencies)/len(numerical_frequencies)
print "Average frequency of whole wave: %.4f Hz" % average_numerical_frequency
print "Frequency between each maxima: ", numerical_frequencies

# Calculating frequency from fourier transformation:
F = np.fft.fft(y_time, time_steps)/time_steps
freq_array = np.fft.fftfreq(time_steps, d=dt)
F = ( 2*np.abs(F[:time_steps/2]) )**2
plt.axis([0,2,0,1.2])
plt.xlabel('Frequency [Hertz]')
plt.ylabel('Fourier coefficient [m^2]')
plt.title('Frequency Domain of 100th mass point')
plt.axvline(x=freq, ls = '--', color = 'k', label = 'Analytical Frequency')
plt.plot(freq_array[:time_steps/2], F, 'o', label = 'Fourrier Frequency')
plt.legend()
plt.savefig('../fig/100_point_fourier.pdf')
plt.clf()

plt.axis([0,1,0,0.001])
plt.xlabel('Frequency [Hertz]')
plt.ylabel('Fourier coefficient [m^2]')
plt.title('Frequency Domain of 100th mass point')
plt.axvline(x=freq, ls = '--', color = 'k', label = 'Analytical Frequency')
plt.plot(freq_array[:time_steps/2], F, 'o', label = 'Fourrier Frequency')
plt.legend()
plt.savefig('../fig/100_point_fourier2.pdf')
plt.clf()
