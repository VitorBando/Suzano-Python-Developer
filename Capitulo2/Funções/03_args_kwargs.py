
def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    menssagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(menssagem)

exibir_poema(
    'Sexta-feira, 15 de Agosto de 2025',
    'Zen of Python',
    'Beatiful is better than ugly.',

    autor = 'Tim Peters',
    ano=1999,

)