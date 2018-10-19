import numpy as np
import matplotlib.pyplot as plt

N = 200  # Number of strings between mass-points.
time_steps = 1200
dt = 0.01
m = 0.02  # Mass of each mass-point. Constant in this run.
k = 10.0  # Spring constant.
i = np.array(range(N))
lamb = 200/3.5

def y_init_cond(i):
    # Initial Conditions of string at t=0.
    value = np.zeros(len(i))
    for n in range(len(i)):
        if n >= 70 and n <= 99:
            value[n] = (n-69)/30.0
        elif n >= 100 and n <= 128:
            value[n] = (129-n)/30.0
        else:
            value[n] = 0
    return value

y_min = y_init_cond(i)
y_0 = y_init_cond(i)
y_plus = np.zeros(N)

beta = k*dt**2/m

for t in range(time_steps):
    y_plus[1:-1] = beta*(-2*y_0[1:-1] + y_0[:-2] + y_0[2:]) + 2*y_0[1:-1] - y_min[1:-1]
    y_min[:] = y_0
    y_0[:] = y_plus

    if t == 0:
        plt.plot(i, y_0, label='$t=%.1f\,s$' % (t*dt))
    elif t%20 == 0 and 0 < t < 200:
        plt.plot(i, y_0, ls='--')
    elif t == 200:
        plt.plot(i, y_0, label='$t=%.1f\,s$' % (t*dt))
        plt.legend()
        plt.axis([0, N, -1, 1])
        plt.title('Triangle function, first 2 seconds')
        plt.xlabel('Mass point number')
        plt.ylabel('Amplitude [meters]')
        plt.savefig('../fig/triangle_collapse.pdf')
        plt.clf()

    if t == 200:
        plt.plot(i, y_0, label='$t=%.1f\,s$' % (t*dt))
    elif t%40 == 0 and 0 < t < 840:
        plt.plot(i, y_0, ls='--')
    elif t == 840:
        plt.plot(i, y_0, label='$t=%.1f\,s$' % (t*dt))
        plt.legend()
        plt.title('Triangle function, seconds 2 to 8.4')
        plt.xlabel('Mass point number')
        plt.ylabel('Amplitude [meters]')
        plt.axis([0, N, -1, 1])
        plt.savefig('../fig/triangle_collapse2.pdf')
        plt.clf()
