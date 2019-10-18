import time
import numpy as np
import matplotlib.pyplot as plt
from tools import solve_lower_triangular, solve_upper_triangular
from Cholesky import least_squares_cholesky
from QR import least_squares_QR
np.random.seed(42)

### Setting up the data.
n = 30
start = -2
stop = 2
x = np.linspace(start, stop, n)
eps = 1

r1 = np.random.uniform(0, 1, n)*eps
r2 = np.random.uniform(0, 1, n)*eps

y1 = x*(np.cos(r1 + 0.5*x**3) + np.sin(0.5*x**3))
y2 = 4*x**5 - 5*x**4 - 20*x**3 + 10*x**2 + 40*x + 10 + r2

## Running the two solvers for m=3 and m=8, and plotting the solutions.
for m in [3, 8]:
    A = np.zeros((n, m))
    for i in range(m):
        A[:,i] = x**i

    for y_nr in range(2):
        y = [y1, y2][y_nr]

        beta = least_squares_cholesky(A, y)
        plt.scatter(x, y, c="crimson", label="Data")
        result = A@beta
        plt.plot(x, result, label=f"Polyfit degree {m}")
        plt.legend()
        plt.savefig(f"../plots/cholesky_y{y_nr}_m={m}.png")
        plt.clf()

        beta = least_squares_QR(A, y)
        plt.scatter(x, y, c="crimson", label="Data")
        result = A@beta
        plt.plot(x, result, label=f"Polyfit degree {m}")
        plt.legend()
        plt.savefig(f"../plots/QR_y{y_nr}_m={m}.png")
        plt.clf()



# Doing a timing of the two solvers for n=1000 over different ms.
n = 1000
start = -2
stop = 2
x = np.linspace(start, stop, n)
eps = 1
r = np.random.uniform(0, 1, n)*eps
y = 4*x**5 - 5*x**4 - 20*x**3 + 10*x**2 + 40*x + 10 + r

time_QR = []
time_cholesky = []
error_QR = []
error_cholesky = []

m_list = np.logspace(1.8, 2.85, 15, dtype=int)
for m in m_list:
    print(m)
    A = np.zeros((n, m))
    for i in range(m):
        A[:,i] = x**i

    t0 = time.time()
    least_squares_cholesky(A, y)
    time_cholesky.append(time.time() - t0)

    t0 = time.time()
    least_squares_QR(A, y)
    time_QR.append(time.time() - t0)


time_QR = np.log10(np.array(time_QR))
time_cholesky = np.log10(np.array(time_cholesky))
m_log = np.log10(np.array(m_list))
plt.plot(m_log, time_QR, "bo")
plt.plot(m_log, time_cholesky, "ro")
c1, c0 = np.polyfit(m_log, time_QR, 1)
plt.plot(m_log, c0 + m_log*c1, label=f"QR, slope = {c1:.2f}", c="b")
c1, c0 = np.polyfit(m_log, time_cholesky, 1)
plt.plot(m_log, c0 + m_log*c1, label=f"Choleksy, slope = {c1:.2f}", c="r")
plt.legend()
plt.title("Runtime comparison for n=1000 points")
plt.ylabel("Log(Time), [seconds]")
plt.xlabel("Log(poly_order)")
plt.savefig("../plots/timings.png")
