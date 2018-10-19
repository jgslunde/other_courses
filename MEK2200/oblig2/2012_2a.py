import matplotlib.pyplot as plt
from numpy import linspace, meshgrid
from matplotlib.lines import Line2D

### Vector field ###
def field(x, y, a, b):
    return b+a*y, a+b*x
b = 0.1
for a in [0, 0.1, 0.2, 0.3]:
    x, y = meshgrid(linspace(-1, 1, 16), linspace(-1, 1, 16))
    u, v = field(x, y, a, b)
    plt.figure()
    Q = plt.quiver(x, y, u, v, units='width', pivot='mid')
    plt.axis("equal")
    plt.axis([-1.1, 1.1, -1.1, 1.1])
    plt.title("Displacement field $u(x,y) = [\\beta + \\alpha y, \\alpha + \\beta x]$ for $\\alpha = %s$, $\\beta = %s$" % (a, b))
    plt.savefig("fig/field_a=%sb=%s.pdf" % (a,b))
    plt.clf()

### Displacement of square ###
def plot_shape(points):
    fig = plt.figure()
    for i in range(len(points)):
        plt.plot([points[-i][0], points[-i+1][0]], [points[-i][1], points[-i+1][1]], 'b-')
        plt.plot(points[i][0], points[i][1], "ro")

points = [[-1,0], [0,1], [1,0], [0,-1]]

b = 0.1
for a in [0, 0.1, 0.2, 0.3]:
    new_points = []
    for x, y in points:
        u, v = field(x, y, a, b)
        x_displaced = x + u
        y_displaced = y + v
        new_points.append([x_displaced, y_displaced])
    plot_shape(new_points)
    plt.axis("equal")
    plt.axis([-2, 2, -2, 2])
    plt.grid("on")
    plt.title("Displacement of square for $\\alpha = %s$, $\\beta=%s$" % (a,b))
    plt.savefig("fig/square_a=%sb=%s.pdf" % (a,b))
    plt.clf()
