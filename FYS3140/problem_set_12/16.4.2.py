from numpy import pi, sin, cos, linspace
import matplotlib.pyplot as plt

def B(n):
	return (2*sin(n*pi/4) - sin(n*pi/2))/n**2

def y(x, t, N, h=1, v=1, L=1):
	value = 0
	for n in range(1, N):
		value += B(n)*sin(n*pi*x/L)*cos(n*pi*v*t/L)
	return 8*h/pi**2 * value

x = linspace(0,10,1000)

for t in linspace(0,1,10):
	plt.plot(x, y(x, t, 1000))
plt.show()
