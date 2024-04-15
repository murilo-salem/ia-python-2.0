import scipy.constants as const

def TempoQueda(H):

    G = const.g
    T = (2 * H / G) ** 0.5
    return T

# Test cases
TestCase = [1, 10, 0, -1]
for Times in TestCase:
    Tempo = TempoQueda(Times)
    print(f"Para H = {Times} m, o tempo estimado é de {Tempo:.3f} segundos.")
