import numpy as np
import matplotlib.pyplot as plt

passos = 50
x = np.zeros(passos + 1)
y = np.zeros(passos + 1)
x[0], y[0] = 0, 0.4

r = 3.5

for i in range(passos):
    y[i + 1] = r * y[i] * (1 - y[i])
    x[i + 1] = x[i] + 1

fig, ax = plt.subplots()
ax.plot(x, y, alpha=0.5)
ax.set(xlabel='Tempo (anos)', ylabel='População (fração do máximo)')
plt.title(f"Mapa Logístico (r = {r:.2f})")
plt.show()
