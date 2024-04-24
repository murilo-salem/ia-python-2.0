def base_alternativa(N):
    def p_n(x, n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= (i - x)
        return resultado

    for n in range(N + 1):
        yield lambda x, n=n: p_n(x, n)

print("Base Alternativa para P^4:")
for indice, polinomio in enumerate(base_alternativa(4)):
    print(f"p_{indice}(x) = {polinomio(0)}")
