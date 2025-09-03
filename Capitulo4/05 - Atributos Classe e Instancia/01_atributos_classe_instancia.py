class Estudante():
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

a1 = Estudante('Vitor', 1)
a2 = Estudante('Ana', 2)

mostrar_valores(a1, a2)

a1.escola = 'Python'
a3 = Estudante('Roger', 3)
mostrar_valores(a1, a2, a3)