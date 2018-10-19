# Shows the effect of an increasing number of AC-generators to form an electric pulse.
# The pulse is formed by adding sinus curves on the form 1/(2n+1)*sin((2n+1) t) together,
# with n from 1 and up.

import os
import numpy as np
import matplotlib.pyplot as plt
import imageio

N = 100	# Highest desired amounts of AC-generators(and thereby sinus curves)
time_steps = 100001
time = np.linspace(0,np.pi, time_steps)	# Uniformally spaced time.
sinus_curves = np.zeros( shape = (N, time_steps) )	# Empty array for sinus curves


def AC_sinus(time, n):
	# Returns Sinus-curve as an array from a given constant n and a time-array.
	return 1.0/(2*n+1) * np.sin((2*n+1)*time)

for n in range(N):
	# Each new curve is the sum of the former and current n.
	sinus_curves[n] = sinus_curves[n-1] + AC_sinus(time,n)

def plot_raise_time(Hz = 1, skip_n = 5):
	# Plots the raise time of pulses as a function of numer of AC-generators,
	# given a refresh rate of the AC-current.
	# skip_n allowes to ignore the first few values, as they will have very high raise times.
	last_sinus = sinus_curves[-1]
	pulse_top = last_sinus[time_steps/2] # Defines the top of the pulse as the middle of the last curve
	ten_percent_raised = 0.1*pulse_top
	ninety_percent_raised = 0.9*pulse_top
	raise_times = np.zeros(N)
	for n in range(N):
		for i in range(time_steps):
			if sinus_curves[n,i] > ten_percent_raised:
				ten_percentile = i
				break
		for i in range(ten_percentile, time_steps):
			if sinus_curves[n,i] > ninety_percent_raised:
				ninety_percentile = i
				break
		raise_times[n] = (ninety_percentile - ten_percentile) / float(time_steps*Hz)

	plt.plot( np.linspace(0, N-1, N)[skip_n:], raise_times[skip_n:] )
	plt.title( "Time for %dHz pulse to raise from 10 to 90 percent height." % Hz )
	plt.xlabel( "Number of AC-generators" )
	plt.ylabel( "Raise time (seconds)" )
	plt.grid()
	plt.show()


def make_gif():
	# Making a gif
	filenames = []
	images = (range(1,40))
	images += (range(41,100, 2))
	images += (range(101,1000, 20))
	print images
	for i in (images):
		plt.plot(time, sinus_curves[i])
		plt.axis([-0.1, np.pi+0.1, 0, 1])
		plt.title("n = %d" % i)
		plt.savefig("fig/pulse%d.png" % i)
		plt.clf()
		filenames.append("fig/pulse%d.png" % i)
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	imageio.mimsave("fig/pulse.gif", images)
	for filename in filenames:
		os.remove(filename)

plot_raise_time()
