def Eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

"""
def Expoentes_de_primos_de_Mersenne(limite):
    expoentes = []
    for k in range(2, limite + 1):
        if Eh_primo(2 ** k - 1):
            expoentes.append(k)
    return expoentes
"""

def Expoentes_de_primos_de_Mersenne(limite):
    expoentes = []
    for k in range(2, limite + 1):
        if Eh_primo(2 ** k - 1) and 2 ** k - 1 <= limite:
            expoentes.append(k)
    return expoentes


def Numeros_perfeitos(limite):
    numeros_perfeitos = []
    for k in Expoentes_de_primos_de_Mersenne(13):
        numeros_perfeitos.append(2 ** (k - 1) * (2 ** k - 1))
    return numeros_perfeitos


numeros_perfeitos = Numeros_perfeitos(10000)
print("Números perfeitos menores que 10.000 escritos na forma exigida:")
print(numeros_perfeitos)
