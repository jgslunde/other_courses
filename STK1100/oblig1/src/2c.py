import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("dodelighet-felles.txt")[1:]
data = np.transpose(data)
ald, q_x = data

def F(x):
    value = 1
    for y in range(x+1):
        value *= (1-q_x[y+35]/1000)
    return 1 - value

p = np.zeros(72)
for x in range(72):
    p[x] = F(x) - F(x-1)

plt.plot(ald[35:], p)
plt.xlabel("X")
plt.ylabel("p(X)")
plt.savefig("../2c.pdf")