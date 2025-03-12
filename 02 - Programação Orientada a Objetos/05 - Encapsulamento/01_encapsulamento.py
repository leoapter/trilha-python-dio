# Encapsulamento: Proteção aos dados de um objeto
# Agrupar dados e métodos que manipulam esses dados
# Impoe restrições de acesso publico direto a variáveis e metodos
# Evitar modificação acidenta de dados
# Avariavel so pode alterada pelo método desse objeto
# Acesso privado: sinal - : so pode ser acessado pela classe
# Acesso público: sinal + : pode ser acessado de forra da classe
# No Python não existe palavra reservada para encapsulamento, pore´exite convenção
# A princípio todos os recursos são públicos, 
# a não ser que esteja antecedido do "underline" (_)
# Ex: def__init__(self, saldo=0):
#       self._saldo = saldo  <--- acesso privado
# Porem não há garantia de que não poderá ser acessado e manipulado. 
# Porque o Python na prática não garante a proteção

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor   # acesso privado

    def mostrar_saldo(self):   
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
