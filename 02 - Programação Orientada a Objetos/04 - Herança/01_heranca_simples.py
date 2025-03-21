# Herança Simles
# Classe filha que deriva ou herda as características e comportamentos da classe pai (base)
# Benefícios: representa bem os relacionamentos da vida real
# Fornece a reutilização de código, Não precisamos escrever novamente o mesmo código repetidamente
# ** Permite adicionar mais resursos a uma classe, sem modifica-la
# ** È de natureza transitiva: Se a classe B herdar da classe A, todas as subclasses de B hersarão automaticamente da classe A
# Sintaxe:
# class A:
#   pass
#
# class B(A):
#   pass

class Veiculo:                # Criando e inicializando a classe Veiculo
    def __init__(self, cor, placa, numero_rodas): # 
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo): # Criando classe "filha", que herda características e comportamentos da classe "pai"
    pass


class Carro(Veiculo):       # Criando classe "filha", quw herda características e comportamentos da classe "pai"
    pass


class Caminhao(Veiculo):    # Aqui a classe "filha", além de herdar as características e comportamentos da classe "pai", está criando/adicionando as suas próprias características.
    def __init__(self, cor, placa, numero_rodas, carregado): # Construindo e inicializando um novo conjunto de atributos, acrescentado o atributo/característica "carregado"
        super().__init__(cor, placa, numero_rodas)  # Palavra reservada para herdar os atributos da classe pai, para evitar que seja sobreescrito alterações após modificações na classe filha
        self.carregado = carregado  # Atribui o valor carregado para o atributo self.carregado

    def esta_carregado(self):  # Criando um novo método, para verificar se está carregado ou não 
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
