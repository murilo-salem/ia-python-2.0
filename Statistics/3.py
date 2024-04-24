import matplotlib.pyplot as plt
import numpy as np

x1_values = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y1_values = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2_values = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y2_values = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3_values = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y3_values = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

x4_values = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4_values = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]


def linha_de_regressao(x, y):
    coeffs = np.polyfit(x, y, 1)
    return np.poly1d(coeffs)


fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Quarteto de Anscombe")

conjuntos_de_dados = [(x1_values, y1_values), (x2_values, y2_values), (x3_values, y3_values), (x4_values, y4_values)]
for i, (x, y) in enumerate(conjuntos_de_dados):
    ax = axs[i // 2, i % 2]
    ax.scatter(x, y, label=f"Conjunto de Dados {i + 1}")
    ax.plot(x, linha_de_regressao(x, y)(x), color='red', linestyle='--', label="Linha de Melhor Ajuste")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

plt.tight_layout()
plt.show()
