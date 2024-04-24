import matplotlib.pyplot as plt


def mapa_logistico(x0, r, N):
    sequencia = [x0]
    for _ in range(1, N):
        xn = sequencia[-1]
        proximo_xn = r * xn * (1 - xn)
        sequencia.append(proximo_xn)
    return sequencia


x0 = 0.5
N = 2000

sequencia_r_1p5 = mapa_logistico(x0, 1.5, N)
sequencia_r_3p5 = mapa_logistico(x0, 3.5, N)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(sequencia_r_1p5[-100:], label="r = 1.5", marker='o', linestyle='-', color='b')
plt.title("Últimos 100 membros da Sequência do Mapa Logístico (r = 1.5)")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(sequencia_r_3p5[-100:], label="r = 3.5", marker='o', linestyle='-', color='r')
plt.title("Últimos 100 membros da Sequência do Mapa Logístico (r = 3.5)")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()

plt.tight_layout()
plt.show()
