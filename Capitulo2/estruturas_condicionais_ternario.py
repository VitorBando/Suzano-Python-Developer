# 'Retorno se condição for atendida' if {condição} else  'Retorno da condição não atendida'

saldo = 2000
saque = 25100

status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realizar o saque!')