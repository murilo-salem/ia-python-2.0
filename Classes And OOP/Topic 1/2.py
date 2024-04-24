class Eqint:
    def __init__(self, objeto):
        self.objeto = objeto

    def __eq__(self, outro):
        if isinstance(outro, Eqint):
            return self.objeto == outro.objeto
        return False

    def __repr__(self):
        return f"Eqint({len(self.objeto)})"

objeto_zero = Eqint([])

objeto_lista = Eqint([1])
objeto_tupla = Eqint((1,))
objeto_string = Eqint('1')

print(objeto_lista == objeto_zero)
print(objeto_tupla == objeto_zero)
print(objeto_string == objeto_zero)

print(objeto_lista == objeto_tupla)
print(objeto_lista == objeto_string)
print(objeto_tupla == objeto_string)

print(objeto_zero)
print(objeto_lista)
print(objeto_tupla)
print(objeto_string)
