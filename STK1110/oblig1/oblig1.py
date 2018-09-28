import numpy as np
import matplotlib.pyplot as plt

age = np.array([249, 254, 243, 268, 253, 269, 287, 241, 273, 306, 303, 280, 260, 256, 278, 344, 304, 283, 310])
n = len(age)
N = 1000000

sample = np.random.choice(age, size=(N,n), replace=True)

averages = np.sort(np.mean(sample, axis=1))
stds = np.sort(np.std(sample, axis=1))

averages_conf_int = (averages[int(0.05*N-1)], averages[int(0.95*N-1)])
stds_conf_int = (stds[int(0.05*N-1)], stds[int(0.95*N-1)])

plt.hist(stds, bins=n*2)
plt.show()

print(averages_conf_int)
print(stds_conf_int)