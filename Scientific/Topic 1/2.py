import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dvdt(v, t, sigma, rho, beta):
    x, y, z = v
    fx = sigma * (y - x)
    fy = x * (rho - z) - y
    fz = x * y - beta * z
    return [fx, fy, fz]

sigma = 10
beta = 8 / 3

valores_rho = [13, 14, 15, 28]

v0 = [1, 1, 1]

t = np.linspace(0, 100, 10000)

for rho in valores_rho:

    sol = odeint(dvdt, v0, t, args=(sigma, rho, beta))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(f'Sistema de Lorenz (rho={rho})')
    plt.show()
