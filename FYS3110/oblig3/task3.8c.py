import matplotlib.pyplot as plt

from numpy import matrix, identity, sort, shape, diag, arange
from numpy.linalg import eig
N = 20
V = 4
g = 1

kets = identity(N)

bra0 = matrix(kets[0])
ket0 = bra0.T
H = - V*ket0*bra0

for i in xrange(N-1):
	ket = matrix(kets[i]).T
	ket_p1 = matrix(kets[i+1]).T
	bra = matrix(kets[i])
	bra_p1 = matrix(kets[i+1])

	H -= g* (ket*bra_p1 + ket_p1*bra)


### Task c)
eig_vals, eig_vecs = eig(H)
plt.plot(eig_vals, "bo")
#plt.show()


### Task d)
ground_state = matrix(eig_vecs[:,0])
P_0 = (bra0*ground_state)**2
bra1 = matrix(kets[1])
P_1 = (bra1*ground_state)**2
print P_0, P_1


## Task e)
X = diag(arange(N))
expec_val_ground_state = ground_state.T*X*ground_state
print expec_val_ground_state
