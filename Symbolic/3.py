import numpy as np
import matplotlib.pyplot as plt

valores_t = np.linspace(0, 1, 100)

valores_n = range(2, 11)
for n in valores_n:
    M_t = np.exp(n * valores_t)
    plt.plot(valores_t, M_t, label=f"n = {n}")

plt.xlabel("t")
plt.ylabel("M(t)")
plt.title("Soluções Específicas para M'(t) = kM(t)")
plt.legend()
plt.grid(True)
plt.show()
