import math

class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, outro):
        mmc = self.denominador * outro.denominador // math.gcd(self.denominador, outro.denominador)

        soma_numeradores = self.numerador * (mmc // self.denominador) + outro.numerador * (mmc // outro.denominador)

        mdc = math.gcd(soma_numeradores, mmc)
        return Racional(soma_numeradores // mdc, mmc // mdc)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


frac1 = Racional(1, 2)
frac2 = Racional(1, 3)
frac3 = Racional(1, 6)

resultado = frac1 + frac2 + frac3
print(resultado)
