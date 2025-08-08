# If / if else / elif
MAIOR_IDADE = 18
MAIOR_IDADE_EMANCIPADO = 16

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')

if idade < MAIOR_IDADE:
    print('Menor de idade, não pode tirar a CNH')

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
else:
    print('Menor de idade, não pode tirar a CNH')

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
elif idade >= MAIOR_IDADE_EMANCIPADO:
    print('Você é menor de idade, porem pode fazer aulas práticas.')
else:
    print('Menor de idade, não pode tirar a CNH')