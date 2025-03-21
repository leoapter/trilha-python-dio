# Método de classe e método estático
# Método de classe é um método que recebe a classe como primeiro argumento
# Método estático é um método que não recebe a classe como primeiro argumento
# Quando devemos utilizar o metodo de classe?
# Quando precisamos acessar a classe, mas não precisamos acessar a instância da classe
# Quando queremos criar métodos de fábrica. Retornam instências de classe
# Quando devemos utilizar o metodo estático?
# Quando não precisamos acessar a instância e nem a classe. Os objetos recebem valores e não referências
# Quando queremos criar funções utilitárias que não dependem de nenhum atributo da classe ou da instância 

# Sintaxe metodo de classe: (aponta para a classe, cls)
# @classmethod
# def nome_do_metodo(cls, argumentos):
#     pass

# Sinta método estático: (não aponta para a classe, não aponta para a instância)
# @staticmethod
# def nome_do_metodo(argumentos):
#     pass

class Pessoa:     # Classe
    def __init__(self, nome, idade): # Método construtor
        self.nome = nome             # Atributos
        self.idade = idade           # Atributos

    @classmethod  # Método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): # Método de classe
        idade = 2022 - ano      # Variável idade
        return cls(nome, idade) # Retorno da classe

    @staticmethod # Método estático. A referência é estática (18)
    def e_maior_idade(idade): # Método estático
        return idade >= 18    # Retorno (da idade)


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)
print()

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
print()

# Pessoa.e_maior_idade() # "chamando a classe"."chamando o método"(valor).
# Veja que nesse caso, a classe é @classmetod e o método é @staticmetod
Pessoa.e_maior_idade(18)
Pessoa.e_maior_idade(17)
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(17))
