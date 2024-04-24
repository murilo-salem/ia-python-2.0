class Eqint:
    def __init__(self, sequencia):

        self.sequencia = sequencia

    def exibir(self):

        return f"Comprimento da sequência: {len(self.sequencia)}"

    def iguais(self, outro):

        return len(self.sequencia) == len(outro.sequencia)

    def adicionar(self, outro):

        sequencia_combinada = self.sequencia + outro.sequencia
        return Eqint(sequencia_combinada)

a = Eqint([1, 2, 3])
b = Eqint([4, 5, 6])

print(a.exibir())
print(a.iguais(b))
c = a.adicionar(b)
print(c.exibir())
