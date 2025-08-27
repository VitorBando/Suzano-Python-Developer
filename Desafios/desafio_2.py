# Desafio implementar apenas 3 operações:
#  limitar transações diarias
#  informar caso ultrapasse a quantidade de transações
#  adicionar data nas transações do extrato

# importando datetime
from datetime import datetime

menu = '''

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
=> '''

saldo = 0
extrato = ''
numero_saques = 0
quantidade_transacoes = 0
data_atual = datetime.now()
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500
TRANSACOES_DIARIAS = 10


while True:

    opcao = int(input(menu))


    if opcao == 1:
        if quantidade_transacoes < TRANSACOES_DIARIAS:
            valor_deposito = int(input('Digite o valor para depósito: '))
            if valor_deposito < 0:
                print('Valor inválido, tente novamente.')
            else:
                quantidade_transacoes += 1
                saldo += valor_deposito
                extrato += f'\n{data_atual} | Depósito: R$ {valor_deposito:.2f}'
        else:
            print('Quantidade de transações diárias excedidas.')
    elif opcao == 2:
        if quantidade_transacoes < TRANSACOES_DIARIAS:
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
                extrato += f'\n{data_atual} | Saque: R$ {valor_saque:.2f}'                
        else:
            print('Quantidade de transações diárias excedidas.')
    elif opcao == 3:
        print(f'''===== EXTRATO =====
              {extrato}\n\nSaldo: {saldo:.2f}
===================
               ''')
    elif opcao == 0:
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desajada.')
    