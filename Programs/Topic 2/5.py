def CalcularDerivadaAproximada(f, x, delta):

    f_superior = f(x + delta)
    f_inferior = f(x - delta)

    AproximacaoDerivada = (f_superior - f_inferior) / (2 * delta)

    return AproximacaoDerivada