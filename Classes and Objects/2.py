class Eqint:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def exibir(self):
        return f"O comprimento do inteiro da sequência é {len(self.sequencia)}"

    def iguais(self, outro):
        return len(self.sequencia) == len(outro.sequencia)


objeto_zero = Eqint([])

um_lista = Eqint([1])
um_tupla = Eqint((1,))
um_string = Eqint('1')

print("O objeto zero é igual ao objeto lista de um:", objeto_zero.iguais(um_lista))
print("O objeto zero é igual ao objeto tupla de um:", objeto_zero.iguais(um_tupla))
print("O objeto zero é igual ao objeto string de um:", objeto_zero.iguais(um_string))

print("O objeto lista de um é igual ao objeto tupla de um:", um_lista.iguais(um_tupla))
print("O objeto lista de um é igual ao objeto string de um:", um_lista.iguais(um_string))
print("O objeto tupla de um é igual ao objeto string de um:", um_tupla.iguais(um_string))

print(objeto_zero.exibir())
print(um_lista.exibir())
print(um_tupla.exibir())
print(um_string.exibir())
