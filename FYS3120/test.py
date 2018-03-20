import numpy as np

x = np.zeros((3,3))
y = np.zeros((3,1))
print(type(x))
print(type(y))
print(x*y)
x = np.matrix(x)
y = np.matrix(y)
print(type(x))
print(type(y))

z = x*y
print(z)