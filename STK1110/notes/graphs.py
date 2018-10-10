import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as st
import numpy as np

# ['seaborn-darkgrid', 'seaborn-ticks', 'ggplot', 'seaborn', 'bmh' 'dark_background']:
plt.style.use("seaborn-darkgrid")
mpl.rcParams["font.family"] = "serif"
np.random.seed(92)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(10)

x = np.linspace(1, 9, 1001)
y = st.norm.pdf(x, 5, 1.5)
ax.plot(x, y, label="$f(x)$")

x = np.random.normal(5, 1.5, 35)
y = np.zeros(35)
ax.plot(x, y, 'ro', label="$X_i$")

plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.legend(fontsize=12)
plt.savefig("figs/RV:1.pdf", bbox_inches="tight")
plt.clf()





fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_yticklabels([])
ax.set_aspect(2)

np.random.seed(6)
x = np.random.normal(5, 1.5, 15)
y = np.zeros(15) + 0.1
plt.axvline(x=np.mean(x), color="k", ls="-", label="mean 1")
ax.plot(x, y, "ko")

np.random.seed(22)
x = np.random.normal(5, 1.5, 15)
y = np.zeros(15)
plt.axvline(x=np.mean(x), color="y", ls="-", label="mean 2")
ax.plot(x, y, "yo")

np.random.seed(42)
x = np.random.normal(5, 1.5, 15)
y = np.zeros(15) - 0.1
plt.axvline(x=np.mean(x), color="r", ls="-", label="mean 3")
ax.plot(x, y, "ro")

ax.axis([0, 10, -0.5, 0.15])
plt.legend(fontsize=9)
plt.savefig("figs/RV:2.pdf", bbox_inches="tight")