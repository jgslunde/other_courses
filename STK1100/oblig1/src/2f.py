import numpy as np
import matplotlib.pyplot as plt

def h(X):
    if X < 35:
        return 0
    else:
        return 1e5/1.03**35 * (1-(1/1.03)**(X-34))/(1-1/1.03)

data = np.genfromtxt("dodelighet-felles.txt")[1:]
data = np.transpose(data)
ald, q_x = data

def F(x):
    value = 1
    for y in range(x+1):
        value *= (1-q_x[y+35]/1000)
    return 1 - value

p = np.zeros(72)
for x in range(72):
    p[x] = F(x) - F(x-1)


E_h_X = 0
for x in range(72):
    E_h_X += h(x)*p[x]

print(E_h_X)

"""
jonas@ubuntu:~/github/other_courses/STK1100/oblig1/src$ python3 2f.py
387141.5341685992
"""