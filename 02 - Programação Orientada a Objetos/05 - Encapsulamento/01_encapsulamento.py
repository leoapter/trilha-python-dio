# Encapsulamento: Proteção aos dados de um objeto
# Agrupar dados e métodos que manipulam esses dados
# Impoe restrições de acesso publico direto a variáveis e metodos
# Evitar modificação acidental de dados
# A variavel só pode alterada pelo método desse objeto
# Acesso privado: sinal - : so pode ser acessado pela classe
# Acesso público: sinal + : pode ser acessado de forra da classe
# No Python não existe palavra reservada para encapsulamento, porém exite uma convenção
# A princípio todos os recursos são públicos, 
# a não ser que esteja antecedido do "underline" (_)
# Ex: def__init__(self, saldo=0):
#       self._saldo = saldo  <--- acesso privado
# Porem não há garantia de que não poderá ser acessado e manipulado. 
# Porque o Python na prática não garante a proteção

class Conta:
    def __init__(self, nro_agencia, saldo=0): # Estamos criando 2 atributos. O atributo saldo só pode ser modificado atraves dos métodos depositar e sacar.
                                              # O primeiro atributo é positional(sempre), o segundo atributo é kw)
        self.nro_agencia = nro_agencia
        self._saldo = saldo 

    def depositar(self, valor): # Método depositar altera o valor do saldo
        # ...
        self._saldo += valor    # Convenção de acesso privado

    def sacar(self, valor):     # Método sacar altera o valor do saldo
        # ...
        self._saldo -= valor    # convenção de acesso privado

    def mostrar_saldo(self):    # Método que recupera o valor do saldo
        # ...
        return self._saldo      # Retorna o valor saldo


conta = Conta("0001", 100)      # Dando um nome, criando uma instância na classe Conta e atribuindo valores aos 2 atributos da instância (nro_agencia e saldo) so podem ser acessados pela classe
                                # Porém um programador com acesso ao código fonte consegue faze-lo...
conta.depositar(200)            # Chamando o módulo depositar e atribuindo valor ao depósito
                                # O valor atribuido ao depósito altera o valor do do saldo, conforme atribuido na função depositar (self._saldo += valor)

print(conta.nro_agencia)        # Invocando o atributo nro_agencia da classe conta
print(conta.mostrar_saldo())    # Invocando o método mostrar_saldo da classe conta
