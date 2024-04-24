def Divisores(n):
    lista_divisores = []
    for i in range(1, n):
        if n % i == 0:
            lista_divisores.append(i)
    return lista_divisores


for i in range(16, 21):
    print(f"Divisores de {i}: {Divisores(i)}")
