import numpy as np
import matplotlib.pyplot as plt


def iteracoes_mandelbrot(N):
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    iteracoes = np.zeros(Z.shape)

    for i in range(N):
        for j in range(N):
            c = Z[i, j]
            z = 0

            for k in range(100):
                z = z ** 2 + c
                if abs(z) >= 2:
                    iteracoes[i, j] = k
                    break

    return iteracoes


N = 1000
iteracoes_mandelbrot = iteracoes_mandelbrot(N)

plt.figure(figsize=(8, 8))
plt.imshow(np.log1p(iteracoes_mandelbrot[400:600, 400:600]), extent=(-1, 1, -1, 1), cmap='hot', origin='lower')
plt.colorbar(label='Logaritmo das Iterações')
plt.title('Conjunto de Mandelbrot (Logaritmo das Iterações)')
plt.xlabel('Real')
plt.ylabel('Imaginário')
plt.show()
