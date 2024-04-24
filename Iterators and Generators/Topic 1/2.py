def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def contar_primos_gemeos(limite):
    contador = 0
    for i in range(3, limite, 2):
        if eh_primo(i) and eh_primo(i + 2):
            contador += 1
    return contador


limite = 1000
quantidade_primos_gemeos = contar_primos_gemeos(limite)
print("Número de primos gêmeos com p2 <", limite, ":", quantidade_primos_gemeos)
