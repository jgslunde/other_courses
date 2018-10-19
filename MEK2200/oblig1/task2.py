from sympy import Matrix, symbols

a, b, d, e = symbols('a b d e')

P = Matrix( [a, b, 0],
            [b, d, 0],
            [0, 0, e] )

print (P)
