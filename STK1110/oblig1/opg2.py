import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st




def get_hit_rate(n, N, alpha=0.05, mu=1, sigma=1):
    data = np.random.normal(loc=mu, scale=sigma, size=(N, n))

    alpha = 0.05
    df = n - 1

    t_ppf_lower = st.t.ppf(1 - alpha/2, df)
    t_ppf_upper = st.t.ppf(alpha/2, df)

    X_bar = np.mean(data, axis=1)
    S = np.std(data, axis=1)

    conf_int = np.zeros((N,2))
    conf_int[:,0] = X_bar - t_ppf_lower*S/np.sqrt(n)
    conf_int[:,1] = X_bar - t_ppf_upper*S/np.sqrt(n)

    does_contain_mu = (conf_int[:,0] < mu) * (mu < conf_int[:,1])
    hit_rate = np.sum(does_contain_mu)/N

    return hit_rate


# TASK 2c)
print( get_hit_rate(n=8, N=1000) )

# TASK 2d)
print( get_hit_rate(n=30, N=1000) )
print( get_hit_rate(n=200, N=1000) )

#data = np.random.e