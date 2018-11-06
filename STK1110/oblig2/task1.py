import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as st
plt.style.use("seaborn-darkgrid")

N = 10
alpha = 0.05
df = N - 1
men = np.array([36.1, 36.3, 36.4, 36.6, 36.6, 36.7, 36.7, 37.0, 36.5, 37.1])
women = np.array([36.6, 36.7, 36.8, 36.8, 36.7, 37.0, 37.1, 37.3, 36.9, 37.4])
both = np.concatenate((men, women), axis=None)

x_bar = np.mean(men)
y_bar = np.mean(women)
s1 = np.std(men)
s2 = np.std(women)
sboth = np.std(both)
t_crit = st.t.ppf(alpha/2, df)

print("Mean men = ", x_bar)
print("Mean women = ", y_bar)
print("Std men = ", s1)
print("Std women = ", s2)
print("Std both = ", both)

print("t-statistic (equal variance) = ", (x_bar - y_bar)/np.sqrt(2*sboth**2/N) )

print("5% rejection region critical value = ", st.t.ppf(alpha/2, df))

print("P-value (equal variance)", 2*st.t.cdf(-2.33, df))

print("P-value (different variance)", 2*st.t.cdf(-2.11, df))


print("s2^2/s1^2 = ", s2**2/s1**2)
"""
print((s1**2 + s2**2)**2/(s1**4 + s2**4)*(N-1) )

df2 = 17

print(st.t.ppf(alpha/2, df2))
"""

print("CDF of f-dist = ", 2*st.f.cdf(s2**2/s1**2, N-1, N-1))

print("Predication Interval = ", x_bar - y_bar + t_crit*np.sqrt(s1**2/N + s2**2/N), x_bar - y_bar - t_crit*np.sqrt(s1**2/N + s2**2/N))

ax = plt.gca()
ax.boxplot([men,women])
ax.set_xticklabels(["Men", "Women"])
plt.ylabel("Body Temperature")
plt.savefig("figs/task1a.pdf")
plt.clf()

ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
st.probplot(men, plot=ax1)
st.probplot(men, plot=ax2)
plt.savefig("figs/task1b.pdf")