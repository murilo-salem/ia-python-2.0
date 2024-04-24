def Divisores(n):
    lista_divisores = []
    for i in range(1, n):
        if n % i == 0:
            lista_divisores.append(i)
    return lista_divisores


def Encontrar_numeros_perfeitos(limite):
    numeros_perfeitos = []
    for i in range(2, limite):
        if sum(Divisores(i)) == i:
            numeros_perfeitos.append(i)
    return numeros_perfeitos


numeros_perfeitos = Encontrar_numeros_perfeitos(10000)
print("Números perfeitos menores que 10.000:", numeros_perfeitos)
