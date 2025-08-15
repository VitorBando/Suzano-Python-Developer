def exibir_mensagem():
    print('Olá, mundo!')

def exibir_mensagem_2(nome):
    print(f'Ola, {nome}! Seja bem vindo!')

def exibir_mensagem_3(nome='Anonimo'):
    print(f'Ola, {nome}! Seja bem vindo!')

exibir_mensagem()
exibir_mensagem_2('Vitor')
exibir_mensagem_3()
exibir_mensagem_3('Vitor')