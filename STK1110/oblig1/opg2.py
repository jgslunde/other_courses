import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

n = 8
N = 1000
mu = 1


# TASK 2c)
data = np.random.normal(loc=mu, scale=1.0, size=(1000,8))

alpha = 0.05
df = n - 1

t_ppf_lower = st.t.ppf(1 - alpha/2, df)
t_ppf_upper = st.t.ppf(alpha/2, df)

X_bar = np.mean(data, axis=1)
S = np.std(data, axis=1)

conf_int = np.zeros((N,2))
conf_int[:,0] = X_bar - t_ppf_lower*S/np.sqrt(n)
conf_int[:,1] = X_bar - t_ppf_upper*S/np.sqrt(n)

does_contain_X = np.zeros(N)
does_contain_X = np.greater(conf_int[:,1], X_bar) * np.greater(X_bar, conf_int[:,0])

does_contain_mu = (conf_int[:,0] < mu) * (mu < conf_int[:,1])
hit_rate = np.sum(does_contain_mu)/N
print(hit_rate)


# TASK 2d)