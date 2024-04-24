import numpy as np


def dvdt(v, t, parametros):
    sigma, rho, beta = parametros
    x, y, z = v
    fx = sigma * (y - x)
    fy = x * (rho - z) - y
    fz = x * y - beta * z
    return np.array([fx, fy, fz])
