from math import factorial
from numpy import zeros, sum

def Omega_func( N, q ):
    return ( factorial(q+N-1) / (factorial(q)*factorial(N-1)) )

N_A = 2
N_B = 2
q = 6
Omega_A = zeros(q+1)
Omega_B = zeros(q+1)
Omega = zeros(q+1)
q_A = range(q+1)
for _q_A in q_A:
    _q_B = q - _q_A
    Omega_A[_q_A] = Omega_func(N_A, _q_A)
    Omega_B[_q_A] = Omega_func(N_B, _q_B)

Omega = Omega_A*Omega_B
Omega_tot = sum(Omega)
P_qA = Omega/Omega_tot

with open("task_e.dat", "w") as outfile:
    outfile.write("%10s%10s%10s%10s%10s\n" % ("q_A", "OmegaA", "OmegaB", "Omega", "P(qA)"))
    outfile.write("-"*10*6 + "\n")
    for i in range(q+1):
        outfile.write("%10d%10d%10d%10d%10.3f\n" % (q_A[i], Omega_A[i], Omega_B[i], Omega[i], P_qA[i]))
