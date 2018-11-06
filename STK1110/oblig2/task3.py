import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as st

#plt.style.use("bmh")
plt.style.use("seaborn-darkgrid")

strength = np.array([40.20, 38.30, 30.20, 18.50, 28.20, 35.30, 27.30, 28.10, 35.00, 16.70])
temp = np.array([290, 270, 240, 210, 250, 260, 220, 210, 250, 210])
pressure = np.array([12, 12, 12, 20, 16, 12, 12, 10, 12, 20])
N = len(temp)
temp_range = max(temp)-min(temp); strength_range = max(strength)-min(strength); pressure_range = max(pressure)-min(pressure)

### TASK 3A ###
cm = plt.cm.get_cmap("jet")
ax = plt.gca()
ax.set_aspect(0.9 * temp_range/strength_range)
sc = ax.scatter(temp, strength, c=pressure, vmin=10, vmax=20, cmap=cm)
plt.xlabel("Temperature")
plt.ylabel("Strength")
plt.colorbar(sc)
plt.savefig("figs/task3a1.pdf", bbox_inches="tight")
plt.clf()

ax = plt.gca()
st.probplot(strength, plot=ax)
plt.savefig("figs/task3a2.pdf")
plt.clf()

ax = plt.gca()
ax.set_aspect(0.5 * pressure_range/strength_range)
ax.plot(pressure, strength, "bo")
plt.savefig("figs/task3a3.pdf", bbox_inches="tight")
plt.clf()


### TASK 3B ###
b1, b0 = np.polyfit(temp, strength, 1)
print("Coefficients, b0, b1 = ", b0, b1)

def lin_reg(x, b0, b1):
    return b0 + b1*x

lin_temps = np.linspace(210, 290, 10)
fit = lin_reg(lin_temps, b0, b1)

ax = plt.gca()
ax.set_aspect(0.5 * temp_range/strength_range)
ax.plot(np.linspace(210, 290, 10), fit, "g")
ax.plot(temp, strength, "bo")
plt.xlabel("Temperature")
plt.ylabel("Strength")
plt.savefig("figs/task3b.pdf", bbox_inches="tight")
plt.clf()


### TASK 3C ###
alpha1 = 0.05
alpha2 = 0.10
Sxx = np.sum(temp**2) - np.sum(temp)**2/N
S = np.sum((strength - lin_reg(temp, b0, b1))**2)/(N-2)
S_beta = S/np.sqrt(Sxx)
print(S_beta)
t_alpha1 = st.t.ppf(alpha1/2, df=N-2)
t_alpha2 = st.t.ppf(alpha2/2, df=N-2)
CI1 = [b1 + t_alpha1*S_beta, b1 - t_alpha1*S_beta]
CI2 = [b1 + t_alpha2*S_beta, b1 - t_alpha2*S_beta]
print("Confidence Interval for alpha=0.05 = ", CI1)
print("Confidence Interval for alpha=0.10 = ", CI2)



### TASK 3D ###
x_bar = np.mean(temp)
x_star = np.linspace(210, 290, 1001)
s = np.std(strength)

S_hat_Y = s*np.sqrt(1/N + (x_star - x_bar)**2/Sxx)

Y_hat = lin_reg(x_star, b0, b1)

mu_Y_x_star = [Y_hat + t_alpha1*S_hat_Y,\
               Y_hat - t_alpha1*S_hat_Y]

pred_int = [Y_hat + t_alpha1*np.sqrt(S_hat_Y**2 + s**2),\
            Y_hat - t_alpha1*np.sqrt(S_hat_Y**2 + s**2)]

ax = plt.gca()
ax.set_aspect(0.8)
ax.plot(np.linspace(210, 290, 10), fit, "k", label="Linear fit")
ax.plot(np.linspace(210, 290, 1001), mu_Y_x_star[0], "y--")
ax.plot(np.linspace(210, 290, 1001), mu_Y_x_star[1], "y--", label="95% CI")
ax.plot(np.linspace(210, 290, 1001), pred_int[0], "g--")
ax.plot(np.linspace(210, 290, 1001), pred_int[1], "g--", label="95% Pred.Int.")
ax.plot(temp, strength, "bo", label="Data sample")
plt.axis([205, 295, 0, 70])
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("Strength")
plt.savefig("figs/task3d.pdf", bbox_inches="tight")
plt.clf()


for _temp in [210, 240, 270]:
    S_hat_Y = s*np.sqrt(1/N + (_temp - x_bar)**2/Sxx)
    Y_hat = lin_reg(_temp, b0, b1)
    mu_Y_x_star = [Y_hat + t_alpha1*S_hat_Y,\
                   Y_hat - t_alpha1*S_hat_Y]
    pred_int2 = [Y_hat + t_alpha1*np.sqrt(S_hat_Y**2 + s**2),\
                Y_hat - t_alpha1*np.sqrt(S_hat_Y**2 + s**2)]
    print("CI for temp %s is %.2f, %.2f of size %.2f" % (_temp, mu_Y_x_star[0], mu_Y_x_star[1], mu_Y_x_star[1]-mu_Y_x_star[0]))
    print("Pred.Int. for temp %s is %.2f, %.2f of size %.2f " % (_temp, pred_int2[0],pred_int2[1], pred_int2[1]-pred_int2[0]))



### TASK 3E ###
strength_mean = np.mean(strength)
t_alpha = st.t.ppf(alpha1/2, df=N-1)
strength_std = np.std(strength)

pred_int_new = [strength_mean + t_alpha*strength_std*np.sqrt(1 + 1/N),
            strength_mean - t_alpha*strength_std*np.sqrt(1 + 1/N)]

print("Prediction interval assuming norm.dist: ", pred_int_new)


ax = plt.gca()
ax.set_aspect(0.8)
ax.plot(np.linspace(210, 290, 10), fit, "k", label="Linear fit")
ax.plot(np.linspace(210, 290, 1001), pred_int[0], "g--")
ax.plot(np.linspace(210, 290, 1001), pred_int[1], "g--", label="95% Pred.Int.")
ax.plot([210, 290], [pred_int_new[0], pred_int_new[0]], "m--")
ax.plot([210, 290], [pred_int_new[1], pred_int_new[1]], "m--", label="New 95% Pred.Int.")
ax.plot(temp, strength, "bo", label="Data sample")
plt.axis([205, 295, 0, 70])
plt.legend()
plt.xlabel("Temperature")
plt.ylabel("Strength")
plt.savefig("figs/task3e.pdf", bbox_inches="tight")
plt.clf()