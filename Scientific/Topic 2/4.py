import numpy as np
import matplotlib.pyplot as plt


def conjunto_mandelbrot(N):

    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    mandelbrot = np.ones(Z.shape, dtype=int)

    for i in range(N):
        for j in range(N):
            c = Z[i, j]
            z = 0

            for _ in range(100):
                z = z ** 2 + c
                if abs(z) >= 2:
                    mandelbrot[i, j] = 0
                    break

    return mandelbrot

N = 100
conj_mandelbrot = conjunto_mandelbrot(N)

plt.figure(figsize=(8, 8))
plt.imshow(conj_mandelbrot, extent=(-2, 2, -2, 2), cmap='hot', origin='lower')
plt.colorbar(label='Conjunto de Mandelbrot')
plt.title('Conjunto de Mandelbrot')
plt.xlabel('Real')
plt.ylabel('Imaginário')
plt.show()
