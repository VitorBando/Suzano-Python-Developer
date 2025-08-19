conta_normal = True
conta_universataria = False

saldo = 2000
saque = 2400
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial.')
    else:
        print('Não foi possivel realizaro o saque, saldo insuficiente')
elif conta_universataria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente...')
else:
    print('Sistema não reconheceu seu tipo de conta, entre em contato com suporte.')