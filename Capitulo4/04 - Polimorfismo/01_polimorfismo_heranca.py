class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa')

# FIXME: exemplo ruim do plano de herança 
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando...')

def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())