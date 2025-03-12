# Programação Orientada a Objetos - POO
# 2 conceitos chave; Classes e Objeto
# Classes: O que é: Uma classe é um modelo ou blueprint que define um conjunto de atributos e métodos que serão utilizados para criar objetos.
# Uma classe é uma instância abstrata que define as caractterísticas e comportamentos de um objeto, porém não conseguimos usar diretamente
# Para que serve: A classe serve como uma estrutura para criar objetos. Cada objeto criado a partir da classe tem os atributos e métodos definidos por essa classe.
# o argumento self é uma referência explícita do objeto. pode utilizar outro nome, mas essa é uma convenção e boa prática muito utilizada
# o argumento this é uma referência implícita do objeto

# Sintaxe:
# class NomeDaClasse:
#    def __init__(self, atributo1, atributo2): #  
#        self.atributo1 = atributo1
#        self.atributo2 = atributo2
#       
#    def metodo_exemplo(self):        # é convenção usar o argumento (self) para  a definição do metodo
#        print(self.atributo1)

# Objetos: O que é: Um OBJETO é uma INSTÂNCIA de uma CLASSE. É criado a partir da classe e tem seus próprios ATRIBUTOS e MÉTODOS.
# Os objetos são instâncias utilizáveis, que possuem as características e comportamentos definidos nas classes e podem ser usados
# Para que serve: Objetos representam entidades do mundo real e permitem a utilização prática das classes e seus métodos em um programa.
# Sintaxe:
# meu_objeto = NomeDaClasse(valor1)
#
# Chamando um método do objeto
# meu_objeto.metodo_exemplo()

# métodos são funções que estão dentro de uma classe

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # aqui fica o método construtor
        self.cor = cor           # característica/atributo da classe
        self.modelo = modelo     # característica/atributo da classe
        self.ano = ano           # característica/atributo da classe
        self.valor = valor

    def buzinar(self):                  # comportamento # isso é um método (função dentro de uma classe)
        print("Plim plim...")

    def parar(self):                    # comportamento # isso é um método (função dentro de uma classe
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):                   # comportamento # isso é um método (função dentro de uma classe
        print("Vrummmmm...")
        

    def __str__(self):
       # return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
       # return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}" 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # a vantagem aqui é que seu aumentar ou diminuir os atributos da classe, tudo será automaticamente atualizado
#aqui retorna o nome da classe^   concatena a lista ^    ^ lista chave = valor . aqui foi usado o comprehention (reestudar)

print()
# Criando a instancia b1 para Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600) # isso é uma instância de bicicleta
# Quando eu crio uma instância classe, eu posso atribuir os comportametos/méttodos atribuidos previamente a ela
print(b1.cor, b1.modelo, b1.ano, b1.valor) # pedindo para acessar os atributos da b1
print(b1)
print(type(b1))
b1.buzinar()
b1.correr()
b1.parar()
print()

# Criando a instância b2 para Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189) # atribuindo as características da instância b2 da classe bicicleta
print(b2)
print(type(b2))
b2.correr()
b2.buzinar()
print(b2.cor)
print()
