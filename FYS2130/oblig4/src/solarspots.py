import matplotlib.pyplot as plt
import numpy as np
N = 2017-1700
dt = 1
Fs = 1/dt

times = []
sunspots = []
infile = open('SN_y_tot_V2.0.txt', 'r')
for line in infile:
    cols = line.split()
    times.append( float(cols[0]) )
    sunspots.append( float(cols[1]) )
infile.close()

plt.plot(times, sunspots)
plt.title("Time spectrum of sunspots")
plt.xlabel("Time[Years]")
plt.ylabel("Amplitude")
plt.savefig("../fig/suntimespec.pdf")
plt.clf()

sunspots_f = np.fft.fft(sunspots,N)/N
frekv = (Fs/2.0)*np.linspace(0,1,N/2)
plt.plot(frekv, 2*np.abs(sunspots_f[:N/2]))
plt.title("Frequency spectrum of sunspots")
plt.xlabel("Frequency[1/Years]")
plt.ylabel("Amplitude")
plt.savefig("../fig/sunfreqspec.pdf")
