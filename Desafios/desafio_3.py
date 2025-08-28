# Desafio cria funções para as opções disponiveis
# criar opção e função de cadastrar usuarios
# criar opção e função de cadastrar contas bancarias

# importando datetime
from datetime import datetime
import textwrap

data_atual = datetime.now()

# funções

def menu():
    menu = '''\n
    ================= MENU =================
    [0] - Sair
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Nova Conta
    [5] - Listar Contas
    [6] - Novo Usuário
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, quantidade_transacoes, limite_transacoes_diarias):
    if quantidade_transacoes < limite_transacoes_diarias:
        if valor_deposito < 0:
            print('Valor inválido, tente novamente.')
        else:
            saldo += valor_deposito
            extrato += f'\n{data_atual} | Depósito: R$ {valor_deposito:.2f}'
            print('\n=== Depósito realizado com sucesso ===')
    else:
        print('Quantidade de transações diárias excedidas.')
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite_valor_saque, numero_saques, limite_saques_diarios, quantidade_transacoes, limite_transacoes_diarias):
    if quantidade_transacoes < limite_transacoes_diarias:
        if valor_saque > limite_valor_saque:
            print(f'Valor superior ao limite por saque, tente novamente.')
        elif numero_saques >= limite_saques_diarios:
            print(f'Limite de saques diários atingido')
        elif valor_saque > saldo:
            print(f'Saldo insuficiente. Saldo atual: {saldo:.2f}')    
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'\n{data_atual} | Saque: R$ {valor_saque:.2f}'    
    else:
        print('Quantidade de transações diárias excedidas.')
    return saldo, extrato

def exibir_extrato(saldo, / , *, extrato):
    print(f'''==========================EXTRATO===========================
                {extrato}\n\n\nSaldo: {saldo:.2f}
============================================================
                ''')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF: ').replace('.','').replace(',','').replace('-','')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n Não foi possível criar usuário, já existe usuário para esse CPF!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf':cpf, 'endereco':endereco})

    print ('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n === Conta criada com Sucesso! ===')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}

    print('\nFalha na criação de conta, usuário inexistente!')        
    
    return

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE = 500
    LIMITE_TRANSACOES_DIARIAS = 10
    AGENCIA = '0001'

    saldo = 0
    extrato = ''
    numero_saques = 0
    quantidade_transacoes = 0
    usuarios = []
    contas = []    

    while True:

        opcao = int(menu())
        
        if opcao == 1:
            valor_deposito = float(input('Digite o valor para depósito: '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato, quantidade_transacoes, LIMITE_TRANSACOES_DIARIAS)
            quantidade_transacoes += 1
            
        elif opcao == 2:           
            valor_saque = float(input('Digite o valor para saque: '))
            saldo, extrato = sacar(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite_valor_saque = LIMITE_VALOR_SAQUE,
                numero_saques = numero_saques,
                limite_saques_diarios = LIMITE_SAQUES_DIARIOS,
                quantidade_transacoes = quantidade_transacoes, 
                limite_transacoes_diarias = LIMITE_TRANSACOES_DIARIAS
            )
            quantidade_transacoes += 1
            
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desajada.')
    
main()