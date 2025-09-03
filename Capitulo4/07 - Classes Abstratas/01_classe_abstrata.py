from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
   
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV...')
        print('Ligada')

    def desligar(self):
        print('Desligando TV...')
        print('Desligada')

    @property
    def marca(self):
        return 'LG'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando Ar Condicionado...')
        print('Ligado')

    def desligar(self):
        print('Desligando Ar Condicionado...')
        print('Desligado')

    @property
    def marca(self):
        return 'Eletrolux'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)