import numpy as np


def a(x, v, t, b, k, mass, F):
    # Acceleration of system as function of position, velocity and time.
    return (F(t) - b*v - k*x) / mass


def ForwardEulerStep(x, v, t, dt, b, k, mass, F):
    # Takes a single integration step in position and velocity, with time-length dt, using Forward Euler.
    v_next = v + dt*a(x, v, t, b, k, mass, F)
    x_next = x + dt*v

    return x_next, v_next


def EulerCromerStep(x, v, t, dt, b, k, mass, F):
    # Takes a single integration step in position and velocity, with time-length dt, using Forward Euler.
    v_next = v + dt*a(x, v, t, b, k, mass, F)
    x_next = x + dt*v_next

    return x_next, v_next


def RungeKuttaStep(x, v, t, dt, b, k, mass, F):
    # Same integration step, using Runge Kutta 4.
    k1 = dt * v
    l1 = dt * a(x, v, t, b, k, mass, F)
    k2 = dt * (v + 0.5*l1)
    l2 = dt * a(x + 0.5*k1, v + 0.5*l1, t + dt/2, b, k, mass, F)
    k3 = dt * (v + 0.5*l2)
    l3 = dt * a(x + 0.5*k2, v + 0.5*l2, t + dt/2, b, k, mass, F)
    k4 = dt * (v + l3)
    l4 = dt * a(x + k3, v + l3, t + dt, b, k, mass, F)

    x_next = x + (k1 + 2*k2 + 2*k3 + k4)/6.0
    v_next = v + (l1 + 2*l2 + 2*l3 + l4)/6.0

    return x_next, v_next


def SolveODE(x0, v0, b, k, mass, length, steps, F = lambda t: 0, method = RungeKuttaStep):
    # Solves second order ODE with chosen parimiters.
    # x0 and v0 are initial conditions in meters, b and k are the friction and string constants.
    # length is the length of the simulation in seconds, and steps are the number of time-steps.
    # F is the external force on the system, and method is the prefered integration method.
    time_array = np.linspace(0, length, steps+1)
    pos_array = np.zeros(steps+1)
    vel_array = np.zeros(steps+1)
    pos_array[0] = x0
    vel_array[0] = v0
    dt = float(length)/steps

    for i in range(steps):
        pos_array[i+1], vel_array[i+1] = method(pos_array[i], vel_array[i], time_array[i], dt, b, k, mass, F)

    return pos_array, vel_array, time_array
