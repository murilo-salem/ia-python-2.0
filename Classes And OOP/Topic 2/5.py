class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __mul__(self, outro):

        if isinstance(outro, int):

            return Racional(self.numerador * outro, self.denominador)
        elif isinstance(outro, Racional):

            novo_numerador = self.numerador * outro.numerador
            novo_denominador = self.denominador * outro.denominador
            return Racional(novo_numerador, novo_denominador)
        else:
            raise TypeError("Tipo não suportado para multiplicação")

    def __rmul__(self, outro):

        return self.__mul__(outro)

    def __sub__(self, outro):

        if isinstance(outro, Racional):

            novo_numerador = self.numerador * outro.denominador - outro.numerador * self.denominador
            novo_denominador = self.denominador * outro.denominador
            return Racional(novo_numerador, novo_denominador)
        else:
            raise TypeError("Tipo não suportado para subtração")



meio = Racional(1, 2)
inteiro_dois = 2
meio_negativo = Racional(-1, 2)

resultado1 = meio * inteiro_dois
print(f"{meio} * {inteiro_dois} = {resultado1}")

resultado2 = inteiro_dois * meio
print(f"{inteiro_dois} * {meio} = {resultado2}")

resultado3 = meio - meio
print(f"{meio} - {meio} = {resultado3}")
