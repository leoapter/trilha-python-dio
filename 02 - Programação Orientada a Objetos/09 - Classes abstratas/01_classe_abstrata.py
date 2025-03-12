# Classes Abstratas
# Interfaces são classes abstratas que definem métodos que devem ser implementados por suas subclasses.
# Em Python, uma classe abstrata é uma classe que não pode ser instanciada, mas pode ser herdada.
# Quando transformamos um método em abstrato, transformamos a classe em abstrata.
# Uma classe abstrata é uma classe que contém pelo menos um método abstrato.
# Logo, transformando a classe em classe abstrata, estamos dizendo que ela não poderé mais ser instanciada, mas poderá ser herdada por outras classes.
# Para criar uma classe abstrata em Python, você deve importar o módulo ABC e o decorador abstractmethod do pacote abc.
# O decorador abstractmethod é usado para definir um método abstrato em uma classe abstrata.
# Uma classe abstrata é uma classe que contém pelo menos um método abstrato.

# Contrato de uma classe abstrata:
# - A classe abstrata deve ser herdada por outras classes.
# - A classe abstrata não pode ser instanciada.
# - A classe abstrata deve conter pelo menos um método abstrato.
# - O método abstrato deve ser implementado por suas subclasses.
# - A classe abstrata pode conter métodos concretos.
# - A classe abstrata pode conter propriedades abstratas.
# - A propriedade abstrata deve ser implementada por suas subclasses.
# - A classe abstrata pode conter propriedades concretas.
# - A propriedade concreta não precisa ser implementada por suas subclasses.

# Sintaxe:
# from abc import ABC, abstractmethod
# class NomeDaClasse(ABC):
#     @abstractmethod
#     def nome_do_metodo(self):
#         pass

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC): # Classe abstrata
    @abstractmethod        # Método abstrato
    def ligar(self):       # Método abstrato
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto): # Herança do método abstrato da classe ControleRemoto
    def ligar(self):              # Implementação do método abstrato da classe ControleRemoto
        print("Ligando a TV...")  # Implementação do método abstrato
        print("Ligada!")          # Implementação do método abstrato

    def desligar(self):           # Implementação do método abstrato da classe ControleRemoto
        print("Desligando a TV...")
        print("Desligada!")

    @property          # Definição de uma propriedade abstrata. Simula um método abstrato 
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto): # Herança do método abstrato da classe ControleRemoto
    def ligar(self):                          # Implementação do método abstrato da classe ControleRemoto
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property         # Definição de uma propriedade abstrata. Simula um método abstrato
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
print()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
print()
