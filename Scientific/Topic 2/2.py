def esta_no_conjunto_mandelbrot(c, max_iteracoes=100):
    z = 0
    for _ in range(max_iteracoes):
        z = z * z + c
        if abs(z) >= 2:
            return False
    return True

c_0 = complex(0, 0)
c_1 = complex(2, 2)
c_2 = complex(2, -2)
c_3 = complex(-2, 2)
c_4 = complex(-2, -2)

print("O ponto c = 0 está no conjunto de Mandelbrot:", esta_no_conjunto_mandelbrot(c_0))
print("O ponto c = 2 + 2i está no conjunto de Mandelbrot:", esta_no_conjunto_mandelbrot(c_1))
print("O ponto c = 2 - 2i está no conjunto de Mandelbrot:", esta_no_conjunto_mandelbrot(c_2))
print("O ponto c = -2 + 2i está no conjunto de Mandelbrot:", esta_no_conjunto_mandelbrot(c_3))
print("O ponto c = -2 - 2i está no conjunto de Mandelbrot:", esta_no_conjunto_mandelbrot(c_4))
