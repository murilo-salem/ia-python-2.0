class Eqint:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def exibir(self):
        return f"Comprimento da sequência: {len(self.sequencia)}"

    def iguais(self, outro):
        return len(self.sequencia) == len(outro.sequencia)

seq1 = [1, 2, 3, 4]
seq2 = [10, 20, 30]
eqint1 = Eqint(seq1)
eqint2 = Eqint(seq2)

print(eqint1.exibir())
print(eqint1.iguais(eqint2))
