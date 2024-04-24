import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lorenz(v, t, sigma, rho, beta):
    x, y, z = v
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

sigma, rho, beta = 10, 28, 8/3
t = np.linspace(0, 40, 10000)

v0_1 = np.array([1, 1, 1])
v0_2 = v0_1 + 1e-5

sol1 = odeint(lorenz, v0_1, t, args=(sigma, rho, beta))
sol2 = odeint(lorenz, v0_2, t, args=(sigma, rho, beta))

fig, axs = plt.subplots(4, figsize=(10, 20))

for i in range(4):
    axs[i].plot(t[i*2500:(i+1)*2500], sol1[i*2500:(i+1)*2500, 0], label='x(t) com v(0) = [1, 1, 1]')
    axs[i].plot(t[i*2500:(i+1)*2500], sol2[i*2500:(i+1)*2500, 0], label='x(t) com v(0) = [1, 1, 1] + 1e-5')
    axs[i].legend()
    axs[i].set_xlabel('t')
    axs[i].set_ylabel('x(t)')
    axs[i].set_title(f't em [{10*i}, {10*(i+1)}]')

plt.tight_layout()
plt.show()
