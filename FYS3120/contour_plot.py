import matplotlib.pyplot as plt
from numpy import meshgrid, pi, linspace, cos

def H(phi, p, I=1, m=1, g=9.81, b=1):
    return 0.5*p**2/(m*b**2 + I) - m*g*b*cos(phi) + m*g*b*lambd*phi

p = linspace(-16, 16, 400)
phi = linspace(-4*pi, 4*pi, 400)
p, phi = meshgrid(p, phi)

for lambd in [0, 0.2, 0.5, 1.0]:
    plt.figure(figsize=(5.5,3))
    plt.contour(phi, p, H(phi, p), 20)
    plt.ylabel("$p'_\phi$", size=16)
    plt.xlabel("$\phi$", size=16)
    plt.title("$\lambda=$%.2f" % lambd, size=16)
    plt.tight_layout()
    plt.savefig("fig/lambd=%.2f.pdf" % lambd)

p = linspace(-3, 3, 400)
phi = linspace(pi, 2*pi, 400)
p, phi = meshgrid(p, phi)

for lambd in [0.95, 1.0]:
	plt.figure(figsize=(5.5,3))
	plt.contour(phi, p, H(phi, p), 100)
	plt.ylabel("$p'_\phi$", size=16)
	plt.xlabel("$\phi$", size=16)
	plt.title("$\lambda=$%.2f" % lambd, size=16)
	plt.tight_layout()
	plt.savefig("fig/x_lambd=%.2f.pdf" % lambd)
