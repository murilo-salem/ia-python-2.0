a = 27
b = 84
c = 110
d = 133
e = 144

lado_esquerdo = a ** 5 + b ** 5 + c ** 5 + d ** 5
lado_direito = e ** 5

if lado_esquerdo == lado_direito:
    print("A equação é verdadeira.")
else:
    print("A equação é falsa.")
