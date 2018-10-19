import numpy as np
import matplotlib.pyplot as plt
for dt in [0.001, 0.002, 0.005, 0.01]:
    N = 200  # Number of strings between mass-points.
    m = 0.02  # Mass of each mass-point. Constant in this run.
    k = 10.0  # Spring constant.
    periods = 5  # Chosen number of oscilation periods.
    i = np.array(range(N))
    lamb = 199/3.5
    freq = 1/lamb*np.sqrt(k/m)
    time_steps = int(periods/(freq*dt))

    def y_init_cond(i):
        # Initial Conditions of string at t=0.
        return np.sin(7*i*np.pi/(N-1))

    y_min = y_init_cond(i)
    y_0 = y_init_cond(i)
    y_plus = np.zeros(N)

    beta = k*dt**2/m  # Can initialize beta outside loop because of
                      # constant spring constant.

    Ek = np.zeros(time_steps)
    Ep = np.zeros(time_steps)


    for t in range(time_steps):
        y_plus[1:-1] = beta*(-2*y_0[1:-1] + y_0[:-2] + y_0[2:]) + 2*y_0[1:-1] - y_min[1:-1]
        v = (y_plus - y_min)/(2*dt)
        Ek[t] = np.sum(0.5*m*v**2)
        Ep[t] = 0.5*np.sum((y_0[:-1] - y_0[1:])**2)*k
        y_min[:] = y_0
        y_0[:] = y_plus

    E_total = Ep + Ek
    timepoints = np.linspace(0, time_steps*dt, time_steps)
    plt.plot(timepoints, E_total, label='$E_{tot}$ at $\Delta t = %.3f$s' % dt)

plt.xlabel('Time [Seconds]')
plt.ylabel('Energy [Joule]')
plt.title('Total energy of oscilating systems over five periods')
plt.axis([0, time_steps*dt, 6.0687, 6.071])
plt.legend()
plt.savefig('../fig/energy_cons2.pdf')
plt.clf()

plt.plot(timepoints, Ek, label='$E_k$')
plt.plot(timepoints, Ep, label='$E_p$')
plt.plot(timepoints, E_total, color='r', label='$E_{tot}$')
plt.xlabel('Time [Seconds]')
plt.ylabel('Energy [Joule]')
plt.title('Energy comparison of oscilating system over 5 periods')
plt.legend()
plt.savefig('../fig/energy_cons.pdf')
plt.clf()
