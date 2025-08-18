# Desafio implementar apenas 3 operações:
#  depósito
#  saque 
#  extrato

menu = '''

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
=> '''

saldo = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = int(input('Digite o valor para depósito: '))
        if valor_deposito < 0:
            print('Valor inválido, tente novamente.')
        else:
            saldo += valor_deposito
            extrato += f'\nDepósito: R$ {valor_deposito:.2f}'        
    elif opcao == 2:
        valor_saque = int(input('Digite o valor para saque: '))
        if valor_saque > LIMITE_VALOR_SAQUE:
            print(f'Valor superior ao limite por saque, tente novamente.')
        elif numero_saques >= LIMITE_SAQUES_DIARIOS:
            print(f'Limite de saques diários atingido')
        elif valor_saque > saldo:
            print(f'Saldo insuficiente. Saldo atual: {saldo:.2f}')    
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'\nSaque: R$ {valor_saque:.2f}'                
    elif opcao == 3:
        print(f'''===== EXTRATO =====
              {extrato}\n\nSaldo: {saldo:.2f}
===================
               ''')
    elif opcao == 0:
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desajada.')
    