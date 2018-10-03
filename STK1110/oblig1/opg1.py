import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
age = np.array([249, 254, 243, 268, 253, 269, 287, 241, 273, 306,\
                303, 280, 260, 256, 278, 344, 304, 283, 310])
n = len(age)

# __TASK 1A & 1B
X_bar = np.mean(age)
S = np.std(age)

df = n-1
conf_int_mean = [X_bar - st.t.ppf(0.95, df)*S/np.sqrt(n),\
                 X_bar - st.t.ppf(0.05, df)*S/(np.sqrt(n))]
conf_int_std = [np.sqrt((n-1)/(st.chi2.ppf(0.95, df)))*S,\
                np.sqrt((n-1)/(st.chi2.ppf(0.05, df)))*S]
print(conf_int_mean)
print(conf_int_std)

# __TASK 1C__
N = 1000000

sample = np.random.choice(age, size=(N,n), replace=True)

averages = np.sort(np.mean(sample, axis=1))
stds = np.sort(np.std(sample, axis=1))

averages_conf_int = (averages[int(0.05*N-1)], averages[int(0.95*N-1)])
stds_conf_int = (stds[int(0.05*N-1)], stds[int(0.95*N-1)])

print(averages_conf_int)
print(stds_conf_int)