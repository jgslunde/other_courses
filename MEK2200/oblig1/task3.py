import matplotlib.pyplot as plt
from numpy import linspace, meshgrid
from matplotlib.lines import Line2D

### Vector field ###
a = 0.5
x, y = meshgrid(linspace(-1, 1, 16), linspace(-1, 1, 16))
u = a*y
v = a*x
plt.figure()
Q = plt.quiver(x, y, u, v, units='width', pivot='mid')
plt.axis("equal")
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.title("Displacement field $u(x,y) = [\\alpha y, \\alpha x]$")
plt.savefig("fig/task3_field.pdf")
plt.clf()

### Displacement of square ###
def plot_shape(points):
    fig = plt.figure()
    for i in range(len(points)):
        plt.plot([points[-i][0], points[-i+1][0]], [points[-i][1], points[-i+1][1]], 'b-')
        plt.plot(points[i][0], points[i][1], "ro")

points = [[-1,0], [0,1], [1,0], [0,-1]]
plot_shape(points)
plt.axis("equal")
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.title("Original square $([-1,0], [0,1], [1,0], [0,-1])$")
plt.savefig("fig/task3_square.pdf")
plt.clf()

for a in [0.2, 0.5, 0.8, 1]:
    new_points = []
    for _x,_y in points:
        new_points.append([_x + a*_y, _y + a*_x])
    plot_shape(new_points)
    plt.axis("equal")
    plt.axis([-1.1, 1.1, -1.1, 1.1])
    plt.title("Displacement of square for a = %s" % a, fontsize=20)
    plt.savefig("fig/task3_a=%s.pdf" % a)
    plt.clf()
