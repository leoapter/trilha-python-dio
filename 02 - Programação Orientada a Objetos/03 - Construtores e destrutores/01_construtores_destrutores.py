# Construtores e Destrutores
# O MÉTODO CONSTRUTOR método contrutor é executado quando a instância da classe é criada
# Esse método inicializa o estado do nosso objeto
# Para declarar esse método especial usamos o nome __init__ ("dunder init")
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
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):        # deletando a instância classe
        print("Removendo a instância da classe.")

    def falar(self):
        print("au-au")


def criar_cachorro():                  # criando o método
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Olá mundo!!!")

del c  # usando o destrutor de "maneira forçada" , 
# caso contrário vai destruir somente no final da execução
# independentemente do lugar do código onde ele foi declarado

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()     # "chamando o método"
