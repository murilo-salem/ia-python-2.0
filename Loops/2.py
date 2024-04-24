def EhPrimo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def PrimeiroNaoPrimoMersenne():
    n = 2
    while True:
        NumeroDeMersenne = 2 ** n - 1
        if not EhPrimo(n):
            return n
        if not EhPrimo(NumeroDeMersenne):
            return n
        n += 1


print("O menor n para o qual 2^n - 1 é composto:", PrimeiroNaoPrimoMersenne())
