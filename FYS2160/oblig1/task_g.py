import matplotlib.pyplot as plt
import seaborn
from math import factorial
from numpy import zeros, argmax, max

def Omega( N, q ):
    return ( factorial(q+N-1) / (factorial(q)*factorial(N-1)) )

N_A = 30
N_B = 70
N = N_A + N_B
q = 100

P_qA = zeros(N+1)

possible_states = Omega( N, q )

for q_A in range(q+1):
    q_B = q - q_A
    Omega_A = Omega(N_A, q_A)
    Omega_B = Omega(N_B, q_B)
    P_qA[q_A] = float(Omega_A * Omega_B)/possible_states

print "Most probable microstate is q_A = %d with probability P(qA) = %.4f%%" % (argmax(P_qA), P_qA[argmax(P_qA)]*100)

plt.plot(P_qA)
plt.title("Probability of different microstates")
plt.xlabel("qA")
plt.ylabel("P(qA)")
plt.savefig("task_g.pdf")
