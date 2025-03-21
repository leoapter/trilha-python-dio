# Poliformismo é o princípio que permite que classes derivadas de uma mesma superclasse
# tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes.
# O polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas,
# ou seja, a capacidade de tratar objetos criados a partir de classes diferentes de forma uniforme.
# O polimorfismo é uma característica da programação orientada a objetos
# que permite que uma referência a um objeto de uma superclasse
# seja tratada como um objeto de uma subclasse.
# Poliformismo com Herança

# Sintaxe: class SubClasse(SuperClasse):
# Sintaxe:     def metodo(self):
# Sintaxe:         print("Comportamento da subclasse")

# Exemplo de polimorfismo. Função Biult-in len. Para cada tipo de objeto, dá uma saida diferente
len("python")          # Objeto tipo string      
print(len("python"))
len([10, 20, 30])      # Objeto tipo lista
print(len([10, 20, 30]))
print()

# Poliformismo com herança superclasse  <-- classe
# A herança é automática, mas não é obrigatória...
# O método pode ser sobreescrito
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


def plano_voo(obj): # nova função, fora da classe. recebe um objeto genérico
                    # ATENÇÃO: Todo objeto que for atribuir aqui, precisa ser filho de pássaro e precisa ter o seu método voar implementado
    obj.voar()      # comportamento. O objeto chama o método voar


plano_voo(Pardal()) # declarando a classe
plano_voo(Avestruz())
plano_voo(Aviao())
print()
# ou
p1 = Pardal()      # criando uma variavel para a instância/classe
p2 = Avestruz()
p3 = Aviao()

plano_voo(p1)      # declarando a variável
plano_voo(p2)
plano_voo(p3)

