# Indentação e blocos de código em Python
# A indentação é obrigatória em Python, pois ela define os blocos de código.
# Em Python, os blocos de código são definidos por dois pontos (:) e a identação.
# Cada indentação é feita com 4 espaços ou tabulações.
# A quantidade de espaços ou tabulações deve ser a mesma para todos os blocos de código.
# A indentação é a forma que o Python define o início e o fim de um bloco de código.

# As funções são blocos de código que podem ser chamados e executados em qualquer parte do código.
# As funções são definidas com a palavra reservada def parâmetro(valor):
# As funções podem ou não receber parâmetros e retornar valores.
# As funções podem ser chamadas em qualquer parte do código.
# As funções são muito úteis para reutilizar blocos de código.
# A diferenca entre métodos e funções é que os métodos são funções que pertencem a uma classe.
# Classes são estruturas que definem objetos e suas propriedades e métodos.
# Exemplo de Classe em Python:
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Exemplo de função em Python
def sacar(valor: float): # def é uma palavra reservada em Python para definir funções.
    saldo = 500

    if saldo >= valor:
        print("Saque efetuado!")
        print(f"Você sacou R$ {valor}.")
        saldo -= valor
        print(f"Seu saldo atual é de R$ {saldo}.")
        print("Retire o seu dinheiro.")
        # fim do bloco if
    else:
        print("Saldo insuficiente!")
        print("Você não pode sacar esse valor.")
        # fim do bloco else

    print()
    print("Obrigado por ser nosso cliente, tenha um bom dia!") # Essa função (print) está indentada após o bloco if/else..
    print()                                                    # Essa função faz parte do bloco da função sacar e será executada após o bloco if/else.
# fim da função sacar


def depositar(valor: float):
    saldo = 500
    saldo += valor
    print(f"Depósito de {valor} efetuado!")
    print(f"Seu saldo atual é de R$ {saldo}.")


sacar(100.12) # Chamando a função sacar e atribuindo um valor
depositar(200.25) # Chamando a função depositar e atribuindo um valor