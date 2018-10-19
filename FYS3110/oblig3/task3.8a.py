from numpy import matrix, identity

N = 4
V = 999  # Easially recognizable sample numbers.
g = 11

kets = identity(N)

ket0 = matrix(kets[0]).T
bra0 = ket0.T
H = - V*ket0*bra0


for i in xrange(N-1):
	ket = matrix(kets[i]).T
	ket_p1 = matrix(kets[i+1]).T
	bra = matrix(kets[i])
	bra_p1 = matrix(kets[i+1])

	H -= g* (ket*bra_p1 + ket_p1*bra)

print "\n", H
