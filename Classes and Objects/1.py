class Eqint:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def exibir(self):
        return f"O comprimento inteiro da sequência é {len(self.sequencia)}"

    def iguais(self, outro):
        return len(self.sequencia) == len(outro.sequencia)


seq1 = [1, 2, 3, 4]
seq2 = [5, 6, 7]
seq3 = [8, 9, 10, 11, 12]

eqint1 = Eqint(seq1)
eqint2 = Eqint(seq2)
eqint3 = Eqint(seq3)

print(eqint1.exibir())
print(eqint1.iguais(eqint2))
print(eqint1.iguais(eqint3))