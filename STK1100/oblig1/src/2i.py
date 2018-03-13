import numpy as np
import matplotlib.pyplot as plt

def g(X):
    if X > 34:
        X = 34
    return (1-(1/1.03)**(X+1))/(1-(1/1.03))

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


E_g_X = 0
for x in range(72):
    E_g_X += g(x)*p[x]

print(E_g_X)

"""
jonas@ubuntu:~/github/other_courses/STK1100/oblig1/src$ python3 2i.py
21.564918895029948
"""