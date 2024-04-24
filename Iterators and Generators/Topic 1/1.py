from itertools import count, islice

def eh_primo(n):
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


def primos_gemeos():
    primos = filter(eh_primo, count())
    primo_anterior = next(primos)
    for primo in primos:
        if primo - primo_anterior == 2:
            yield (primo_anterior, primo)
        primo_anterior = primo


gerador_primos_gemeos = primos_gemeos()
for _ in range(10):
    print(next(gerador_primos_gemeos))
