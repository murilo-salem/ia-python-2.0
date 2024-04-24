class Eqint:
    def __init__(self, valor):
        self.valor = valor
        self.sequencia = [self.valor]

    def __add__(self, outro):
        if isinstance(outro, Eqint):
            return Eqint(self.valor + outro.valor)
        elif isinstance(outro, int):
            return Eqint(self.valor + outro)
        else:
            raise ValueError("Só é possível adicionar Eqint ou int a Eqint")

    def __repr__(self):
        return f"Eqint({self.valor})"


eqint1 = Eqint(1)
eqint2 = Eqint(2)
eqint3 = Eqint(3)

resultado = eqint1 + eqint2 + eqint3

print(resultado)
print(resultado.sequencia)
