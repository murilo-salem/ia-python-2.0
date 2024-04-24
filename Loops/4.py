def FatoresPrimosMultiplicidade(n):
    fatores = {}
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            fatores[divisor] = fatores.get(divisor, 0) + 1
            n //= divisor
        else:
            divisor += 1
    return fatores


TestCases = [17, 18, 19, 20]
for num in TestCases:
    fatores_primos = FatoresPrimosMultiplicidade(num)
    print(f"Fatores primos de {num}: {list(fatores_primos.keys())}")


Multiplicidades = FatoresPrimosMultiplicidade(48)
print(f"Multiplicidades dos fatores primos de 48: {Multiplicidades}")
