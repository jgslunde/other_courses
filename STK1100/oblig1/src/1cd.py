from scipy import misc
import numpy as np

p = 18/37
n = 20

def binom(x, n, p):
    """ Binomial probability b(x;n,p)"""
    nCr = misc.comb(n, x)
    return nCr*p**x*(1-p)**(n-x)

def cum_binom(x_min, x_max, n, p):
    """ Cumulative distribution function F(x_min <= x <= x_max)
    for a binomial function b(x;n,p) """
    P_X = 0
    for x in range(x_min, x_max+1):
        P_X += binom(x, n, p)
    return P_X

#___Exercise c___
print( cum_binom(15,20,n,p) )
print( cum_binom(0,5,n,p) )

#___Exercise d___
p = 6/37
EX = 0
for i in range(0,20):
    EX += (cum_binom(i,i,n,p))*500*i
print( cum_binom(5,20,n,p) )
print( cum_binom(0,1,n,p) )

"""
jonas@ubuntu:~/github/other_courses/STK1100/oblig1/src$ python3 1cd.py
0.015385465001631102
0.027464357940763788
0.21400681498120722
0.14151896666419134
"""