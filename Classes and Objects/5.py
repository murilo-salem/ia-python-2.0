class Eqint:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Eqint({self.valor})"


def construir_inteiros_positivos():
    inteiros_positivos = []

    zero = Eqint(0)
    inteiros_positivos.append(zero)

    for i in range(1, 11):
        proximo_inteiro = Eqint(inteiros_positivos[-1].valor + 1)
        inteiros_positivos.append(proximo_inteiro)

    return inteiros_positivos


lista_inteiros_positivos = construir_inteiros_positivos()

eqint_10 = lista_inteiros_positivos[10]
print(f"Eqint(10) = {eqint_10}")
print(f"Sequência interna: {[eqint.valor for eqint in lista_inteiros_positivos]}")
