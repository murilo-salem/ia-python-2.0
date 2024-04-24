class NumeroRacional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __float__(self):
        return self.numerador / self.denominador

racional_1_2 = NumeroRacional(1, 2)
racional_1_3 = NumeroRacional(1, 3)
racional_1_11 = NumeroRacional(1, 11)

print(float(racional_1_2))
print(float(racional_1_3))
print(float(racional_1_11))
