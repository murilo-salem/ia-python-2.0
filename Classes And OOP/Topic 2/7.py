class NumeroRacional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __lt__(self, outro):
        return self.numerador * outro.denominador < outro.numerador * self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


numeros_racionais = [NumeroRacional(n // 2, n) for n in range(2, 12)]

numeros_racionais_ordenados = sorted(numeros_racionais)

for num in numeros_racionais_ordenados:
    print(num)
