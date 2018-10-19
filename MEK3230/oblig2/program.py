import numpy as np
import matplotlib.pyplot as plt

H = np.load("data.npy")

heights = []
widths = []
for Hi in H:
    heights.append(np.max(Hi))
    has_height_boolean_array = Hi > 0.04
    widths.append(np.sum(has_height_boolean_array))
nr_timesteps = len(H)
time_array = np.linspace(0, 8e4, nr_timesteps)


### Task 3.1.5 ###
anal_X = np.power(time_array, 0.2)
plt.loglog(time_array, anal_X, label = "$T^{1/5}$")
plt.loglog(time_array, widths, label="$X_n(T)$ numerical")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Width")
plt.savefig("X_n.pdf")
plt.clf()
anal_H = np.power(np.linspace(1e-14, nr_timesteps, nr_timesteps), -0.2)
plt.loglog(time_array, anal_H, label = "$T^{-1/5}$")
plt.loglog(time_array, heights, label = "$H_n(T)$ numerical")
plt.xlabel("Time")
plt.ylabel("Height")
plt.legend()
plt.savefig("H_n.pdf")
plt.clf()

### Task 3.1.6 ###
grid_dim = len(H[0])
for i in range(nr_timesteps):
    X_scaled = np.linspace(-1, 1, grid_dim)/widths[i]
    H_scaled = H[i]/heights[i]
    plt.plot(X_scaled, H_scaled)
plt.xlabel("Width")
plt.ylabel("Height")
plt.savefig("similiarity.pdf")
plt.clf()
