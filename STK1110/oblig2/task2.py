import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as st
plt.style.use("seaborn-darkgrid")
mpl.rcParams["font.family"] = "bmh"

N = 31
X_bar_D = -3.26
SE_mean = 1.58
print("test-statistic (t-value) = ", X_bar_D/SE_mean)

P = 2*st.t.cdf(X_bar_D/SE_mean, N-1)
print("p-value = ", P)

alpha = 0.05
t_alpha = st.t.ppf(alpha/2, df=N-1)
CI = [X_bar_D + t_alpha*SE_mean, X_bar_D - t_alpha*SE_mean]
print("Confidence Interval = ", CI)