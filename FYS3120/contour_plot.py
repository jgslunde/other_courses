import matplotlib.pyplot as plt
from numpy import meshgrid, pi, linspace, cos

I = 1
m = 1
g = 9.81
b = 1

p = linspace(-10, 10, 400)
phi = linspace(0, 4*pi, 400)

p, phi = meshgrid(p, phi)



for lambd in linspace(0,1.6,9):
    H = 0.5*p**2/(m*b**2 + I) - m*g*b*cos(phi) + m*g*b*lambd*phi
    plt.figure()
    plt.contour(phi, p, H, 16)
    plt.ylabel("$p'_\phi$", size=16)
    plt.xlabel("$\phi$", size=16)
    plt.title("$\lambda=$%.1f" % lambd, size=16)
    plt.tight_layout()
    plt.savefig("fig/lambd=%.1f.pdf" % lambd)