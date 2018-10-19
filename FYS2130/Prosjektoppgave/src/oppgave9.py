import numpy as np
import matplotlib.pyplot as plt

N = 400  # Number of strings between mass-points.
time_steps = 1200
m = np.array([0.02]*199 + [0.06]*199)
k = 10.0  # Spring constant.
i = np.array(range(N))
lamb = 200/3.5
dt = np.sqrt(0.02/k)

def y_init_cond(i):
    # Initial Conditions of string at t=0.
    value = np.zeros(len(i))
    for n in range(len(i)):
        if n >= 1 and n <= 30:
            value[n] = (n)/30.0
        elif n >= 31 and n <= 59:
            value[n] = (60-n)/30.0
        else:
            value[n] = 0
    return value

y_min = np.zeros(N)
y_min[:-1] = y_init_cond(i)[1:]
y_0 = y_init_cond(i)
y_plus = np.zeros(N)
beta = k*dt**2/m  # Can initialize alpha*k outside loop because of constant mass.

for t in range(time_steps):
    y_plus[1:-1] = beta*(-2*y_0[1:-1] + y_0[:-2] + y_0[2:]) + 2*y_0[1:-1] - y_min[1:-1]
    y_min[:] = y_0
    y_0[:] = y_plus

    if t==0:
        plt.plot(i, y_0, color='r', label='$t=%.1f\,s$' % (dt*t))

    if t%40==0 and 0<t<200:
        plt.plot(i, y_0, ls='--')

    if t==200:
        plt.plot(i, y_0, color='g', label='$t=%.1f\,s$' % (dt*t))
        plt.axis([0, N, -1, 1])
        plt.legend()
        plt.xlabel('Mass point number')
        plt.ylabel('Amplitude [meters]')
        plt.title('Moving square against impedance change')
        plt.axhline(y=(1-np.sqrt(3))/(1+np.sqrt(3)), ls='--', color='k')
        plt.axhline(y=2/(1+np.sqrt(3)), ls='--', color='k')
        plt.savefig('../fig/impedance.pdf')
        plt.clf()

    if t==200:
        plt.plot(i, y_0, color='r', label='$t=%.1f\,s$' % (dt*t))
        print "Amplitude of transmitted wave = %.3f m"%(np.max(y_0))
        print "Amplitude of reflected wave = %.3f m"%(np.min(y_0))

    if t%40==0 and 200<t<400:
        plt.plot(i, y_0, ls='--')

    if t==400:
        plt.plot(i, y_0, color='g', label='$t=%.1f\,s$' % (dt*t))
        plt.axis([0, N, -1, 1])
        plt.xlabel('Mass point number')
        plt.ylabel('Amplitude [meters]')
        plt.title('Moving square against impedance change')
        plt.legend()
        plt.axhline(y=(1-np.sqrt(3))/(1+np.sqrt(3)), ls='--', color='k')
        plt.axhline(y=2/(1+np.sqrt(3)), ls='--', color='k')
        plt.savefig('../fig/impedance2.pdf')
        plt.clf()
