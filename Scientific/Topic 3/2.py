import itertools
import matplotlib.pyplot as plt


def contar_combinacoes(ell):
    return ell * (ell - 1) * (ell - 2) * (ell - 3) // 24


valores_ell = list(range(1, 51))
contagem_combinacoes = [contar_combinacoes(ell) for ell in valores_ell]

plt.figure(figsize=(10, 6))
plt.plot(valores_ell, contagem_combinacoes, label='Número de Combinações')
plt.plot(valores_ell, [ell ** 4 for ell in valores_ell], label=r'$\ell^4$')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Comprimento (ell)')
plt.ylabel('Número de Combinações')
plt.title('Número de Combinações vs. Comprimento (ell)')
plt.legend()
plt.grid(True)
plt.show()
