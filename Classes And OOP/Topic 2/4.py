class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __mul__(self, outro):
        num = self.numerador * outro.numerador
        den = self.denominador * outro.denominador

        mdc_val = mdc(num, den)
        return Racional(num // mdc_val, den // mdc_val)


def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


frac1 = Racional(1, 3)
frac2 = Racional(15, 2)
frac3 = Racional(2, 5)

resultado = frac1 * frac2 * frac3
print(resultado.numerador, '/', resultado.denominador)
