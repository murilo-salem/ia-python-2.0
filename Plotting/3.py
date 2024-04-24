import numpy as np
import matplotlib.pyplot as plt

x_0 = 0.5

n_membros = 2000

n_plotagem = 1000

valores_r = np.arange(1, 4.01, 0.01)

ultimos_membros = []

for r in valores_r:
    sequencia = [x_0]
    for _ in range(n_membros):
        x_0 = r * x_0 * (1 - x_0)
        sequencia.append(x_0)
    ultimos_membros.append(sequencia[-n_plotagem:])

plt.figure(figsize=(10, 6))
for i, r in enumerate(valores_r):
    plt.plot([r] * n_plotagem, ultimos_membros[i], 'k.', markersize=2)

plt.xlabel('Valor de r')
plt.ylabel('Valores na sequência')
plt.title('Últimos 1.000 membros da sequência logística para diferentes valores de r')
plt.grid(True)

plt.show()
