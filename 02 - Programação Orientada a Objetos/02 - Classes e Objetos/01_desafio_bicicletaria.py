# Programação Orientada a Objetos - POO
# 2 conceitos chave; Classes e Objeto
# Classes:Uma classe é um modelo ou blueprint que define um conjunto de atributos e métodos que serão utilizados para criar objetos.
# Uma classe é uma instância abstrata que define as caractterísticas e comportamentos de um objeto, porém não conseguimos usar diretamente
# Para que serve: A classe serve como uma estrutura para criar objetos. Cada objeto criado a partir da classe tem os atributos e métodos definidos por essa classe.
# O primeiro argumento de um método de uma classe é o self. O self é uma referência ao objeto que está sendo criado. Ele é usado para acessar os atributos e métodos do objeto.
# Um objeto é uma instância de uma classe. É criado a partir da classe e tem seus próprios atributos e métodos.
# Objetos representam entidades do mundo real e permitem a utilização prática das classes e seus métodos em um programa.
# Métodos são funções que estão dentro de uma classe. Eles definem o comportamento dos objetos criados a partir da classe.
# O método construtor __init__ é um método especial que é chamado quando o objeto é instanciado. Ele é usado para inicializar os atributos do objeto.
# O método especial __str__ é um método que retorna uma string que representa o objeto. Ele é usado para exibir informações sobre o objeto de forma legível.
# O método especial __repr__ é um método que retorna uma string que representa o objeto. Ele é usado para exibir informações sobre o objeto de forma precisa.
# O método especial __eq__ é um método que compara dois objetos. Ele é usado para verificar se dois objetos são iguais.
# O argumento self é uma referência explícita do objeto. pode utilizar outro nome, mas essa é uma convenção, e boa prática muito utilizada
# O argumento this é uma referência implícita do objeto

# Sintaxe:
# class NomeDaClasse:
#    def __init__(self, atributo1, atributo2): # isso é um método construtor. O atributo self é uma referência ao objeto que está sendo criado. O atributo1 e atributo2 são atributos da classe. O primeiro argumento de um método de uma classe é o self. O primeiro argumento é obrigatóriamente posicional e é uma referência ao objeto que está sendo criado  
#        self.atributo1 = atributo1
#        self.atributo2 = atributo2
#       
#    def metodo_exemplo(self):        # é convenção usar o argumento (self) para  a definição do metodo
#        print(self.atributo1)

# Um OBJETO é uma INSTÂNCIA de uma CLASSE. É criado a partir da classe e tem seus próprios ATRIBUTOS e MÉTODOS.
# Os objetos são instâncias utilizáveis, que possuem as características e comportamentos definidos nas classes e podem ser usados
# Para que serve: Objetos representam entidades do mundo real e permitem a utilização prática das classes e seus métodos em um programa.
# Sintaxe:
# meu_objeto = NomeDaClasse(valor1)
# meu_objeto = NomeDaClasse(valor1, valor2)

# Chamando um método do objeto
# meu_objeto.metodo_exemplo()

# Métodos são funções que estão dentro de uma classe
# Eles definem o comportamento dos objetos criados a partir da classe
# O primeiro argumento de um método de uma classe é o self
# Exemplo de método:
# def metodo_exemplo(self):    # No método é obrigatório atribuir ao menos 1 atributo, sendo convenção usar o argumento (self) no atributo0, para  a definição do primeiro ou único atributo.	
#    print(self.atributo1)
#    print(self.atributo2)

class Bicicleta:  
    def __init__(self, cor, modelo, ano, valor): # aqui fica o método construtor. O método construtor é um método especial que é chamado quando o objeto é instanciado
        self.cor = cor           # atributo da classe = característica. O self é uma referência ao objeto que está sendo criado
        self.modelo = modelo     # atributo da classe = caracteristica. O self é uma referência ao objeto que está sendo criado
        self.ano = ano           # atributo da classe = caracteristica. O self é uma referência ao objeto que está sendo criado
        self.valor = valor       # atributo da classe = caracteristica. O self é uma referência ao objeto que está sendo criado

    def buzinar(self):                  # comportamento # Isso é um método da classe Bicicleta. Uma funçao dentro da Classe. Instâncias da Classe bicicleta podem buzinar
        print("Plim plim...")

    def parar(self):                    # comportamento # isso é um método da classe Bicicleta. Instâncias da classe bicicleta podem parar
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):                   # comportamento # isso é um método da classe Bicicleta. Instâncias da classe bicicleta podem correr
        print("Vrummmmm...")
        

    def __str__(self):  # Aqui é um método especial que retorna uma string que representa os objetos da classe bicicleta. Nesse exemplo, os objetos da classe bicicleta são representados por uma string que contém as características da bicicleta:
       # return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
       # return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}" 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # a vantagem aqui é que seu aumentar ou diminuir os atributos da classe, tudo será automaticamente atualizado
#aqui retorna o nome da classe^   concatena a lista ^    ^ lista chave = valor . aqui foi usado o comprehention (reestudar)
print()
      
# Criando a instancia b1 para Bicicleta e atribuindo as características da instância b1 da classe bicicleta
# Quando eu crio uma instância classe, eu posso atribuir os comportametos/méttodos atribuidos previamente a ela
b1 = Bicicleta("vermelha", "caloi", 2022, 600) # isso é uma instância de bicicleta
print(b1.cor, b1.modelo, b1.ano, b1.valor) # pedindo para acessar os atributos da b1 da classe bicicleta para imprimir
print(b1.__dict__) # pedindo para acessar os atributos da b1 da classe bicicleta para imprimir no formato de dicionário
print(b1)
print(type(b1))
b1.buzinar() # pedindo para acessar o método buzinar da b1 da classe bicicleta para imprimir
b1.correr()  # pedindo para acessar o método correr da b1 da classe bicicleta para imprimir
b1.parar()   # pedindo para acessar o método parar da b1 da classe bicicleta para imprimir
print()

# Criando a instância b2 para Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 1890) # atribuindo as características da instância b2 da classe bicicleta
print(b2)
print(type(b2))
b2.correr()
b2.buzinar()
b2.parar()
print(b2.cor)
print(b2.modelo)
print(b2.ano)
print(b2.valor)
print(b2.parar()) # pedindo para acessar o método parar da b2 da classe bicicleta para imprimir
print(b2.__dict__) # pedindo para acessar o método parar da b2 da classe bicicleta para imprimir
print()
