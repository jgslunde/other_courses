from numpy import matrix, sqrt, zeros, complex128

H = matrix([ [  1,   1j/2., 0],
             [-1j/2,  1,   0],
             [   0,     0,   1/2.]])

ket1 = 1/sqrt(2)*matrix([1j, 1, 0]).T
ket2 = matrix([0,0,1+0j]).T
ket3 = 1/sqrt(3)*matrix([-1j, 1, -1]).T

kets = matrix([[1j/sqrt(2),  1j/sqrt(2),  0],
               [0,           0,           1],
               [-1j/sqrt(3), 1/sqrt(3),   -1/sqrt(3)]])

# print (H*ket1) / ket1
# print (H*ket2) / ket2
# print (H*ket3) / ket3

H_new = zeros(shape=(3,3), dtype=complex128)

for i in range(3):
    for j in range(3):
        H_new[i,j] = kets[i]*H*kets[j].T

print H_new
