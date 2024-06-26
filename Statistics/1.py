import numpy as np

conjuntos_de_dados = [
    np.array(
        [[10.0, 8.04], [8.0, 6.95], [13.0, 7.58], [9.0, 8.81], [11.0, 8.33], [14.0, 9.96], [6.0, 7.24], [4.0, 4.26],
         [12.0, 10.84], [7.0, 4.82], [5.0, 5.68]]),
    np.array(
        [[10.0, 9.14], [8.0, 8.14], [13.0, 8.74], [9.0, 8.77], [11.0, 9.26], [14.0, 8.10], [6.0, 6.13], [4.0, 3.10],
         [12.0, 9.13], [7.0, 7.26], [5.0, 4.74]]),
    np.array(
        [[10.0, 7.46], [8.0, 6.77], [13.0, 12.74], [9.0, 7.11], [11.0, 7.81], [14.0, 8.84], [6.0, 6.08], [4.0, 5.39],
         [12.0, 8.15], [7.0, 6.42], [5.0, 5.73]]),
    np.array([[8.0, 6.58], [8.0, 5.76], [8.0, 7.71], [8.0, 8.84], [8.0, 8.47], [8.0, 7.04], [8.0, 5.25], [19.0, 12.50],
              [8.0, 5.56], [8.0, 7.91], [8.0, 6.89]])
]

medias = []
desvios_padrao = []
for conjunto_de_dados in conjuntos_de_dados:
    medias.append(np.mean(conjunto_de_dados))
    desvios_padrao.append(np.std(conjunto_de_dados))

media_corresponde = all(np.isclose(medias, medias[0], atol=0.01))
desvio_padrao_corresponde = all(np.isclose(desvios_padrao, desvios_padrao[0], atol=0.01))

print("As médias correspondem para todos os conjuntos de dados:", media_corresponde)
print("Os desvios padrão correspondem para todos os conjuntos de dados:", desvio_padrao_corresponde)
