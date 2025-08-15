def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca} - {modelo} - {ano} - {placa}.')

salvar_carro('Hyundai', 'HB20', 2020, 'DUE-9F01')
print()
salvar_carro(marca='Hyundai', modelo='HB20', ano=2020, placa='DUE-9F01')
print()
salvar_carro(**{'marca':'Hyundai', 'modelo':'HB20', 'ano':2020, 'placa':'DUE-9F01'})
