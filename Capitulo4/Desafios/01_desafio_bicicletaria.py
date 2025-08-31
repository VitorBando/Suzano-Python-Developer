class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada.')

    def correr(self):
        print('Vrummmmm...')

    # def __str__(self):
    #     return f'Bicicleta\nCor: {self.cor}\nModelo: {self.modelo}\nAno: {self.ano}\nValor: {self.valor}.'
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


b1 = Bicicleta('Vermelha', 'caloi', 2022, 6060)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
    
b2 =  Bicicleta('Verde', 'Monark', 2020, 189)
b2.buzinar()
print(b2)