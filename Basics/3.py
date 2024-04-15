import math

def Fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * Fatorial(numero - 1)  # Forma recursiva

def Stirling(numero):
    return math.sqrt(2 * math.pi) * (numero**(numero + 0.5)) * math.exp(-numero)

ValoresTestCase = [5, 10, 15, 20]

for n in ValoresTestCase:
    Fatorial_resultado = Fatorial(n)
    Stirling_resultado = Stirling(n)
    Erro_Absoluto = abs(Fatorial_resultado - Stirling_resultado)
    Erro_Relativo = Erro_Absoluto / n
    print(f"{n}: Erro Absoluto = {Erro_Absoluto:.6f}, Erro Relativo = {Erro_Relativo:.6f}")
