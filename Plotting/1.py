def mapa_logistico(x0, r, N):
    sequencia = [x0]
    for _ in range(1, N):
        xn = sequencia[-1]
        proximo_xn = r * xn * (1 - xn)
        sequencia.append(proximo_xn)
    return sequencia

x0 = float(input("Digite o valor inicial (x0): "))
r = float(input("Digite a taxa de crescimento (r): "))
N = int(input("Digite o número de membros na sequência (N): "))

sequencia = mapa_logistico(x0, r, N)

print("Sequência do mapa logístico:")
for i, xn in enumerate(sequencia):
    print(f"x_{i}: {xn}")
