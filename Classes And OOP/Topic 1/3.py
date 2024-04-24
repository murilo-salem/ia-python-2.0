class EqInt:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __add__(self, outro):
        sequencia_combinada = self.sequencia + outro.sequencia
        return EqInt(sequencia_combinada)


a = EqInt([1, 2, 3])
b = EqInt([4, 5, 6])

c = a + b
print(c.sequencia)
