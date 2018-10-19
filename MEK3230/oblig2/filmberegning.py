# encoding: utf8
from __future__ import division
import time
from math import pi
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import ode as sp_ode

###############################################################################
# Utgangspunkt for oppgave (e)

L = 6*pi # størrelsen på domenet
n = 600 + 1 # gridpunkt
dx = L/(n - 1) # gridstørrelse
x = np.arange(-L/2, L/2, dx) # x-koordinat
Bo = 1.0e19 # Bond tall
grav = 1.0 # retningen på gravitasjonskraften

# Startverdi og tidsskritt
h0 = 1 - np.tanh(2*(x - 0*3*pi))**2
t0, dt, t1 = 0, 500, 8e4

###############################################################################
# Utgangspunkt for oppgave (i)
#L = 2*pi # størrelsen på domenet
#n = 400 + 1 # gridpunkt
#dx = L/(n - 1) # gridstørrelse
#x = np.arange(-L/2, L/2, dx) # x-koordinat
#Bo = 0.5 # Bond tall
#grav = -1.0 # retningen på gravitasjonskraften
#ki = 1 # bølgetallet til forstyrrelsen/perturbasjonen
#
## Startverdi og tidsskritt
#h0 = 1 + 0.005*np.sin(ki*x)
#t0, dt, t1 = 0, 500, 8e4

###############################################################################
# Høyreside til ligningsløseren

def hoyreside(t, h):
    hx = diff1(h, dx);
    hxxx = diff2(hx,dx);
    s = diff1(-1/Bo*h**3*hxxx + grav*hx*h**3, dx)
    return s

def diff1(y, dx):
    l = len(y)
    i = np.arange(l)
    im1 = np.mod(i-1, l)
    ip1 = np.mod(i+1, l)
    s = (y[ip1] - y[im1])/(2*dx)
    return s

def diff2(y, dx):
    l = len(y)
    i = np.arange(l)
    im1 = np.mod(i-1, l)
    ip1 = np.mod(i+1, l)
    s = (y[ip1] - 2*y[i] + y[im1])/dx**2
    return s

###############################################################################
# Tidsintegrasjon + numerisk diskretisering av ligningen
# t = tid, H = H(X,t) = overflaten

ode = sp_ode(hoyreside)
ode.set_integrator('lsoda', rtol=1e-6, atol=1e-6, first_step=1.0e-4, nsteps=10000)
ode.set_initial_value(h0, t0)

t = []
H = []
print('Beregner, dette tar litt tid ...')
t_start = time.time()
heights = []
widths = []
while ode.successful() and ode.t < t1:
    ti = ode.t
    print(ti)
    Hi = ode.integrate(ti + dt)
    t.append(ti)
    H.append(Hi)
print('Ferdig etter %.2f sekunder!' % (time.time() - t_start))
assert ode.successful()

np.save("data.npy",H)

###############################################################################
# Plot


################
# Startverdi
plt.figure()
plt.plot(x, h0, linewidth=2)
plt.xlabel('X')
plt.ylabel('H(X,T=0)')
plt.title('Startverdi')
plt.axis([-L/2, L/2, 0, 1.1])

################
# Sluttverdi
plt.figure()
plt.plot(x, H[-1], linewidth=2)
plt.xlabel('X')
plt.ylabel('H(X,T=end)')
plt.title('Sluttverdi')
plt.axis([-L/2, L/2, 0, 1.1])

################
# "Film" NB: denne dukker ikke opp på gamle versjoner av matplotlib!
plt.ion()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)

print('Film!')
for ti, Hi in zip(t, H):
    ax.clear()
    ax.plot(x, Hi, linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('H_0(X,T=0)')
    ax.set_title('Overflate H(X,T=%.1f)' % ti)
    plt.axis([-L/2, L/2, 0, 1.1])
    plt.draw()
    plt.pause(0.1)

# Beregn q
q0 = sum(h0)*dx
q1 = sum(H[-1])*dx
print(q0)
print(q1)

plt.ioff()
plt.show()
