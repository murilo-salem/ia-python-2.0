inteiros_positivos = []

class Eqint:
    def __init__(self, sequencia):
        self.sequencia = sequencia


zero = Eqint(inteiros_positivos)
inteiros_positivos.append(zero)

proximo_inteiro = Eqint(list(inteiros_positivos))
inteiros_positivos.append(proximo_inteiro)

for _ in range(9):
    proximo_inteiro = Eqint(list(inteiros_positivos))
    inteiros_positivos.append(proximo_inteiro)

eqint_10 = inteiros_positivos[10]
print(eqint_10)
print(eqint_10.sequencia)
