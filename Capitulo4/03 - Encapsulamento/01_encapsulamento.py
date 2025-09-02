class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nrm_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self):
        return self._saldo


conta = Conta('0001', 0)

conta.depositar(100)
print(conta.mostrar_saldo())
conta.sacar(50)
print(conta.mostrar_saldo())
conta.sacar(100)
print(conta.mostrar_saldo())
print(conta.nrm_agencia)