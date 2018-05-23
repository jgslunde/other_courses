import matplotlib.pyplot as plt
import numpy as np

N = 60
M = 500000

microstates = np.random.choice(np.array([-1,1]), (M,N))

s = np.sum(microstates, axis=1)//2
macrostates = np.zeros(N+1)
for i in range(N+1):
    macrostates[i] = np.sum( s == -N/2+i )

energies = np.arange(-N//2, N//2+1)
gaussian_plot = np.exp(-2*(energies/np.sqrt(N))**2) * np.max(macrostates)
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(energies, macrostates, label="Generated microstates")
ax.plot(energies, gaussian_plot, "r", label="Guass")
plt.title("Multiplicity of energies for N=%d, M=%d system vs gauss curve" % (N, M))
plt.xlabel("Energy [$\mu B$]")
plt.ylabel("Multiplicity $\Omega$")
plt.axis([-N//2, N//2, 0, np.max(macrostates)*1.1])
plt.savefig("task_q.pdf")
