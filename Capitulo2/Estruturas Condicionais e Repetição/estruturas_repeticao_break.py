while True:
    opcao = int(input('Informe um número: '))

    if opcao == 10:
        break 
    if opcao % 2 == 0:
        continue

    print(opcao)


for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=' ')