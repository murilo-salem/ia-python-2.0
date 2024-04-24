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


N = 500
conj_mandelbrot = conjunto_mandelbrot(N)
print(conj_mandelbrot)


def plot_mandelbrot(mandelbrot_set):
    plt.imshow(mandelbrot_set, cmap='twilight_shifted')
    plt.colorbar()
    plt.title('Conjunto de Mandelbrot')
    plt.show()

N = 4000
conj_mandelbrot = conjunto_mandelbrot(N)

plot_mandelbrot(conj_mandelbrot)

