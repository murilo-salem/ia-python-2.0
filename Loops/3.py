def EhPrimo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def PrimosMersenne(n):
    PrimosDeMersenne = []
    for i in range(2, n):
        if EhPrimo(i):
            NumerosDeMersenne = 2 ** i - 1
            if EhPrimo(NumerosDeMersenne):
                PrimosDeMersenne.append((i, NumerosDeMersenne))
    return PrimosDeMersenne


# Encontrando todos os primos de Mersenne com n < 40
NumerosDeMersenne = PrimosMersenne(40)
for Primos in NumerosDeMersenne:
    print(f"n = {Primos[0]} gera um número primo de Mersenne: {Primos[1]}")
