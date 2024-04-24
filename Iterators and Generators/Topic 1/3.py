import math
import matplotlib.pyplot as plt


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


def contar_primos_gemeos(N):
    contador = 0
    for i in range(3, N - 2, 2):
        if eh_primo(i) and eh_primo(i + 2):
            contador += 1
    return contador


valores_N = [2 ** k for k in range(4, 17)]
pi_sobre_N_valores = [contar_primos_gemeos(N) / N for N in valores_N]

plt.figure(figsize=(10, 6))
plt.plot(valores_N, pi_sobre_N_valores, marker='o', linestyle='-')
plt.xscale('log')
plt.xlabel('N (escala logarítmica)')
plt.ylabel('π_N / N')
plt.title('Razão de primos gêmeos para N')
plt.grid(True)
plt.show()
