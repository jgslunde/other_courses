from numpy import exp, pi, linspace
import matplotlib.pyplot as plt
# import seaborn

def r(theta, m=1, psi=1, Gamma=5):
    return exp((m*theta - 2*pi*psi)/Gamma )

theta = linspace(0, 360, 3601)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r(theta))
ax.grid(True)
plt.title("Strømlinjer for $m=1$, $\psi=1$, $\Gamma=5$")
plt.savefig("fig/task_2_1_1.pdf")
