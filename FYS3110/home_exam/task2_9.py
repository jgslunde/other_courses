import matplotlib.pyplot as plt
from numpy import zeros, logspace, int64, log10
from math import sqrt
from scipy import stats

def UF(alpha, beta):
    # Calculates UF(alpha|s> + beta|i*>) = s_coeff|s> + i_coeff|i*>
    # and returns the new coefficients in front of s and i*.
    s_coeff = alpha*(1- 4/N) - 2/sqrt(N)*beta
    i_coeff = alpha*2/sqrt(N) + beta
    return s_coeff, i_coeff

def condition(alpha, beta):
    # Returns the normalization condition on alpha and beta, which should be 1.
    return alpha**2 + beta**2 + 2*alpha*beta/sqrt(N)

def prob_alpha(alpha, N):
    # Returns the probability of measuring a state i*
    return alpha**2*(1/N - 1) + 1

# Plotting the probability for the three Ns.
nr_of_ns = 300
for N in [int(1e3), int(1e4), int(1e5)]:
    alpha = 1
    beta = 0
    prob_array = zeros(nr_of_ns)
    for n in range(nr_of_ns):
        alpha, beta = UF(alpha, beta)
        prob_array[n] = prob_alpha(alpha, N)
    plt.plot(prob_array, label="N=%d" % N)
plt.title("Probability of measuring i* after n applications of UF\nin a N-state system")
plt.xlabel("n - Number of applications of UF")
plt.ylabel("P(i*)")
plt.legend()
plt.savefig("three_Ns.pdf")
plt.clf()

print("%10s%10s" % ("N", "n*"))
for N in [int(1e2), int(1e3), int(1e4), int(1e5), int(1e6), int(1e7), int(1e8)]:
    alpha = 1
    beta = 0
    n_star = 0
    prob = 0
    while prob < 0.99:
        alpha, beta = UF(alpha, beta)
        prob = prob_alpha(alpha, N)
        n_star += 1
    print("%10.0e%10s" % (N, n_star))

Ns = logspace(2, 7, 1000, dtype=int64)
n_stars = zeros(len(Ns))
for i in range(len(Ns)):
    N = Ns[i]
    alpha = 1
    beta = 0
    n_star = 0
    prob = 0
    while prob < 0.99:
        alpha, beta = UF(alpha, beta)
        prob = prob_alpha(alpha, N)
        n_star += 1
    n_stars[i] = n_star

slope, intercept, r_value, p_value, std_err = stats.linregress(log10(Ns), log10(n_stars))

print("Slope of the logaritmic curve = ", slope)

plt.loglog(Ns, n_stars)
plt.title("Required applications of UF onto state\nto aquire 99% probability of measuring i*")
plt.xlabel("N - Number of states in system")
plt.ylabel("n* - Required applications of UF")
plt.savefig("n_star.pdf")
plt.clf()
