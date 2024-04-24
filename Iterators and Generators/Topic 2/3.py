def base_monomial(n):
    for i in range(n + 1):
        yield f"x^{i}" if i > 0 else "1"


base_P3 = list(base_monomial(3))
base_P4 = list(base_monomial(4))


def base_combinada(base_P3, base_P4):
    for m3 in base_P3:
        for m4 in base_P4:
            yield (m3, m4)


base_P3_P4 = list(base_combinada(base_P3, base_P4))

for i, (m3, m4) in enumerate(base_P3_P4):
    print(f"Elemento da base {i + 1}: {m3} × {m4}")
