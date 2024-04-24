import numpy as np

def aproximacao_pi_wallis(N):
    aproximacoes_pi = []
    for n in range(1, N + 1):
        pi_n = 2 * np.prod([(2 * i) ** 2 / ((2 * i - 1) * (2 * i + 1)) for i in range(1, n + 1)])
        aproximacoes_pi.append(pi_n)
    return aproximacoes_pi


aproximacoes = aproximacao_pi_wallis(20)

aproximacoes_ordenadas = sorted(aproximacoes)

print("Lista ordenada de aproximações racionais para π:")
for i, pi_n in enumerate(aproximacoes_ordenadas):
    print(f"π_{i + 1} ≈ {pi_n}")

aproximacoes_flutuantes = np.array(aproximacoes, dtype=np.float64)

pi = np.pi
precisao = pi - aproximacoes_flutuantes

print("\nPrecisão das aproximações (π - aproximações):")
print(precisao)
