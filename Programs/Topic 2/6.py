import math


def f_1(x):
    return math.exp(x)


def DerivadaAproximada(f, x, delta):
    return (f(x + delta) - f(x)) / delta


DerivadaNoPonto = 1

# Test cases.
Valores = range(1, 8)
for n in Valores:
    Delta = 10 ** (-2 * n)
    DerivadaAproximadaN = DerivadaAproximada(f_1, 0, Delta)
    Erro = abs(DerivadaAproximadaN - DerivadaNoPonto)
    print(f"Delta: {Delta:.1e}, Derivada Aproximada: {DerivadaAproximadaN:.7f}, Erro: {Erro:.2e}")
