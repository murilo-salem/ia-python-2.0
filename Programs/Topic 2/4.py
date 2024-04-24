import math


def CalculoQuadratico(numero):
    a = 10 ** (-numero)
    b = 10 ** numero
    c = 10 ** (-numero)

    Discriminante = b ** 2 - 4 * a * c

    if Discriminante >= 0:
        x1 = (-b + math.sqrt(Discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(Discriminante)) / (2 * a)
        return x1, x2
    else:
        return "Raízes complexas."


SolucaoN3 = CalculoQuadratico(3)
print(f"Soluções para n = 3: {SolucaoN3}")

SolucaoN4 = CalculoQuadratico(4)
print(f"Soluções para n = 4: {SolucaoN4}")
