class Monomio:
    def __init__(self, expoente):
        self.expoente = expoente

    def __repr__(self):
        if self.expoente == 0:
            return '1'
        elif self.expoente == 1:
            return 'x'
        else:
            return 'x^{}'.format(self.expoente)

def base_polinomial(N):
    for i in range(N + 1):
        yield Monomio(i)


print("Base para P^3:")
for monomio in base_polinomial(3):
    print(monomio)
