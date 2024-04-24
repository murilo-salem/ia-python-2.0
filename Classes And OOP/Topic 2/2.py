class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.forma_normal()

    def forma_normal(self):
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

        divisor = mdc(abs(self.numerador), self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"


racional1 = Racional(12, 6)
racional2 = Racional(3, 9)
racional3 = Racional(2, 16)

print(racional1)  # Saída: 2/1
print(racional2)  # Saída: 1/3
print(racional3)  # Saída: 1/8
