def esta_no_conjunto_mandelbrot(c, max_iteracoes=100):
    z = 0
    for _ in range(max_iteracoes):
        z = z * z + c
        if abs(z) >= 2:
            return False
    return True

c = complex(0, 0)
print(esta_no_conjunto_mandelbrot(c))
