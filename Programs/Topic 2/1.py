import math

# Valores de x e y
x = 1
y = 1 + 10**(-14) * math.sqrt(3)

LadoEsquerdo = 10**14 * (y - x)
LadoDireito = math.sqrt(3)

# Checando se a igualdade é verdadeira.
if math.isclose(LadoEsquerdo, LadoDireito):
    print("A igualdade é verdadeira!")
else:
    print("A igualdade não é verdadeira.")
