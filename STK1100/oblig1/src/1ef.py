#___Exercise 1e___
P = 0
for Z in range(1,26+1):
    P += (36/37)**(Z-1) * 1/37
print(P)

#___Exercise 1f___
P = 0
for Z in range(1,45+1):
    P += (36/37)**(Z-1) * 1/37
print(1-P)

"""
jonas@ubuntu:~/github/other_courses/STK1100/oblig1/src$ python3 1ef.py
0.5095212523720186
0.2914304665172236
"""