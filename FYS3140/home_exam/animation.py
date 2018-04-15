import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(data, x_axis=None, y_lims=None, T=8):
    """
    x_axis = None / array
    y_lims = None / array / "free"
    """
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'r-', animated=True)

    N, n = np.shape(data)
    interval = 1000*float(T)/N

    if x_axis is None:
        x_axis = np.arange(n)

    def init():
        ax.set_xlim(x_axis[0], x_axis[-1])
        ax.set_ylim(1.1*np.min(data), 1.1*np.max(data))
        return ln,

    def update(frame):
        i = int(frame)
        xdata = x_axis
        ydata = data[i]
        ln.set_data(xdata, ydata)
        if y_lims is "free":
            ax.set_xlim(x_axis[0], x_axis[-1])
            ax.set_ylim(1.1*np.min(ydata), 1.1*np.max(ydata))
        return ln,

    ani = FuncAnimation(fig, update, frames=N,
        init_func=init, blit=True, interval=interval)
    plt.show()


if __name__ == "__main__":
    N = 2000
    n = 400
    x = np.linspace(-10, 10, n)
    t = np.linspace(0, 4, N)
    data = np.zeros((N, n))
    for i in range(N):
        data[i] = np.sin(2*x - 40*t[i])
    animate(data, x)