# entrada de dados
nome = input('Digite seu nome: ') 
idade = input('Digite sua idade: ') 

# saida de dados
print(f'Olá, {nome}! Você tem {idade} anos.')

print(type(nome))
print(type(idade)) # por padrão o input converte os dados para string

# Podemos fazer duas abordagens se for necessário fazer conversão
# 1 convertendo na entrada de dados
idade2 = int(input('Digite sua idade: '))
print(type(idade2))

# 2 convertendo na saida de dados
print(int(idade2))