# Poliformismo é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes.
# O polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas, ou seja, a capacidade de tratar objetos criados a partir de classes diferentes de forma uniforme.
# O polimorfismo é uma característica da programação orientada a objetos que permite que uma referência a um objeto de uma superclasse seja tratada como um objeto de uma subclasse.
# Poliformismo com Herança

# Sintaxe: class SubClasse(SuperClasse):
# Sintaxe:     def metodo(self):
# Sintaxe:         print("Comportamento da subclasse")

class Passaro:             # superclasse
    def voar(self):        # método
        print("Voando...") # comportamento


class Pardal(Passaro):     # subclasse
    def voar(self):        # método
        print("Pardal pode voar") # comportamento


class Avestruz(Passaro):   # subclasse
    def voar(self):        # método
        print("Avestruz não pode voar") # comportamento


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj): # função
    obj.voar()      # comportamento


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())

