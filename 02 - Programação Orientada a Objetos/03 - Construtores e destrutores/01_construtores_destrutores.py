# Construtores e Destrutores
# O MÉTODO CONSTRUTOR método contrutor é executado quando a instância da classe é criada
# Esse método inicializa o estado do nosso objeto
# Para declarar esse método especial usamos o nome __init__ ("dunder init")
# Tudo que for escrito como __nome__ é um método especial do Python
# O primeiro parâmetro de qualquer método de uma classe é a palavra reservada self
# Sintaxe
# class nome_da_classe:
#   def__init__(self, atrib1, atrib2, atrib3...)
#       self.atrib1 = atrib1
#       self.atrib2 = atrib2
#       self.atrib3 = atrib3
#
# O MÉTODO DESTRUTOS é sempre executado quando a instância(objeto) é destruida
# Para declarar esse método especial usamos o nome __del__
# Sintaxe:
# class nome_da _classe:
#   def__del__(self):

class Cachorro:
    def __init__(self, nome, cor, acordado=True):  # inicializando a instância classe
        print("Construindo e inicializando a instância da classe.")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):        # Destruindo a instância classe. 
        print("Removendo as instâncias da classe.") # O termo print aqui é só para visualização. Não é obrigatório. Na prática não se usa print em destrutores.

    def falar(self):
        print("au-au") # O termo print aqui é só para visualização. Será substituído por um método de fala.	

    def andar(self):
        print("andando...")

def criar_cachorro():   # Criando um método para instanciar a classe. Isso fica mais organizado. Está localizado fora da classe.
    c = Cachorro("Zeus", "Branco e preto", False) # criando a instância da classe
    print(c.nome)   # acessando o atributo da instância da classe
    print(c.cor)    # acessando o atributo da instância da classe
    c.falar()       # chamando o método da instância da classe
    c.andar()       # chamando o método da instância da classe

criar_cachorro()     # Chamando o método criar_cachorro, mas afeta somente a instância criada dentro do método. Não afeta a instância criada fora do método.

c = Cachorro("Chappie", "amarelo") # criando a instância da classe
print(c.nome)       # acessando o atributo da instância da classe
print(c.cor)        # acessando o atributo da instância da classe
print(c.acordado)   # acessando o atributo da instância da classe
c.falar()           # chamando o método da instância da classe
c.andar()           # chamando o método da instância da classe

print("Olá mundo!!!")

del c  # usando o destrutor de "maneira forçada" , 
# caso contrário vai destruir somente no final da execução
# independentemente do lugar do código onde ele foi declarado

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

criar_cachorro()     # Chamando novamente o método criar_cachorro, mas afeta somente a instância criada dentro do método. Não afeta a instância criada fora do método. 
