import numpy as np
import matplotlib.pyplot as plt

N = 200
time_steps = 1200
dt = 0.01

m = 0.02  # Mass of each mass-point. Constant in this run.
k = 10.0  # Spring constant. Constant in this run.
i = np.array(range(N))  # Indexes of mass-points.

def y_init_cond(i):
    # Initial Conditions of string at t=0.
    return np.sin(7*i*np.pi/(N-1))

y_min = y_init_cond(i)
y_0 = y_init_cond(i)
y_plus = np.zeros(N)

beta = k*dt**2/m  # Can initialize beta outside loop to save time.

for t in range(time_steps):
    y_plus[1:-1] = beta*(-2*y_0[1:-1] + y_0[:-2] + y_0[2:]) + 2*y_0[1:-1] - y_min[1:-1]
    y_min[:] = y_0
    y_0[:] = y_plus
    if t in [0, 127]:  # First and last point in a half-period
        plt.plot(i, y_0, label = 't=%.1fs' % (t*dt))
    if t in range(9, 127, 9):  # Chosen points in between
        plt.plot(i, y_0, ls = ':')

plt.title('Standing wave oscilation')
plt.legend(loc=1)
plt.ylabel('Amplitude [meters]')
plt.xlabel('Mass point number')
plt.axis([0, N, -1.4, 1.4])
plt.savefig('../fig/sinus_wave.pdf')

"""
# Old, unvectorized code
for t in range(time_steps):
    for j in range(1, N-1):
        y_plus[j] = beta*(-2*y_0[j] + y_0[j-1] + y_0[j+1]) + 2*y_0[j] - y_min[j]
    y_min[:] = y_0
    y_0[:] = y_plus
"""
