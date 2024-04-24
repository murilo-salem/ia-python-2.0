class Eqint:
    def __init__(self, n):
        self.n = n
        self.sequencia = [n]

    def adicionar(self, m):
        self.n += m
        self.sequencia.append(self.n)
        return self

    def __repr__(self):
        return f"Eqint({self.n})"


eqint1 = Eqint(1)
eqint2 = Eqint(2)
eqint3 = Eqint(3)

resultado = eqint1.adicionar(eqint2.n).adicionar(eqint3.n)

print(resultado)

print(resultado.sequencia)
