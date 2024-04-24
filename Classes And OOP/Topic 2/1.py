import math

def forma_normal(numerador, divisor):
    mdc = math.gcd(numerador, divisor)
    return numerador // mdc, divisor // mdc

casos_de_teste = [(3, 2), (15, 3), (20, 42)]

for numerador, divisor in casos_de_teste:
    n, d = forma_normal(numerador, divisor)
    print(f"Original: {numerador}/{divisor}, Forma Normal: {n}/{d}")
