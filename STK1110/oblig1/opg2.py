import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st



N = 1000
alpha = 0.05
mu = 1
sigma = 1
ns = range(8, 200, 4)

#__TASK 2C & 2D___
hit_rates_norm_mean = []
hit_rates_norm_std = []
for n in ns:
    df = n - 1
    
    t_ppf_lower = st.t.ppf(1 - alpha/2, df)
    t_ppf_upper = st.t.ppf(alpha/2, df)
    chi_pdf_lower = st.chi2.ppf(1 - alpha/2, df)
    chi_pdf_upper = st.chi2.ppf(alpha/2, df)

    data = np.random.normal(loc=mu, scale=sigma, size=(N, n))

    X_bar = np.mean(data, axis=1)
    S = np.std(data, axis=1)

    conf_int_mean = np.zeros((N,2))
    conf_int_std = np.zeros((N,2))
    conf_int_mean[:,0] = X_bar - t_ppf_lower*S/np.sqrt(n)
    conf_int_mean[:,1] = X_bar - t_ppf_upper*S/np.sqrt(n)
    conf_int_std[:,0] = np.sqrt((n-1)/(chi_pdf_lower))*S
    conf_int_std[:,1] = np.sqrt((n-1)/(chi_pdf_upper))*S

    does_contain_mu = (conf_int_mean[:,0] < mu) * (mu < conf_int_mean[:,1])
    does_contain_sigma = (conf_int_std[:,0] < sigma) * (sigma < conf_int_std[:,1])
    hit_rates_norm_mean.append( np.sum(does_contain_mu)/N )
    hit_rates_norm_std.append( np.sum(does_contain_sigma)/N )


#__TASK 2E & 2F___
hit_rates_exp_mean = []
hit_rates_exp_std = []
for n in ns:
    df = n - 1
    
    t_ppf_lower = st.t.ppf(1 - alpha/2, df)
    t_ppf_upper = st.t.ppf(alpha/2, df)
    chi_pdf_lower = st.chi2.ppf(1 - alpha/2, df)
    chi_pdf_upper = st.chi2.ppf(alpha/2, df)

    data = np.random.exponential(scale=sigma, size=(N, n))

    X_bar = np.mean(data, axis=1)
    S = np.std(data, axis=1)

    conf_int_mean = np.zeros((N,2))
    conf_int_std = np.zeros((N,2))
    conf_int_mean[:,0] = X_bar - t_ppf_lower*S/np.sqrt(n)
    conf_int_mean[:,1] = X_bar - t_ppf_upper*S/np.sqrt(n)
    conf_int_std[:,0] = np.sqrt((n-1)/(chi_pdf_lower))*S
    conf_int_std[:,1] = np.sqrt((n-1)/(chi_pdf_upper))*S

    does_contain_mu = (conf_int_mean[:,0] < mu) * (mu < conf_int_mean[:,1])
    does_contain_sigma = (conf_int_std[:,0] < sigma) * (sigma < conf_int_std[:,1])
    hit_rates_exp_mean.append( np.sum(does_contain_mu)/N )
    hit_rates_exp_std.append( np.sum(does_contain_sigma)/N )

plt.plot(ns, hit_rates_norm_mean, label="Normal distribution, mean.")
plt.plot(ns, hit_rates_norm_std, label="Normal distribution, std.")
plt.plot(ns, hit_rates_exp_mean, label="Exponential distribution, mean.")
plt.plot(ns, hit_rates_exp_std, label="Exponential distribution, std.")
plt.axhline(y=0.95, ls='--', color='r')
plt.ylabel("Confidence")
plt.xlabel("Sample sizes")
plt.legend()
plt.savefig("opg2.pdf")