# Variaveis de classe e variveis de instancia
# Variaveis de classe são compartilhadas por todas as instancias de uma classe
# Variaveis de instancia são unicas para cada instancia
# Atributos de classe são definidos fora de qualquer metodo
# Atributos de instancia são definidos dentro de um metodo construtor
# O que é uma classe? É um modelo que define os atributos e comportamentos de um objeto
# O que é um objeto? É uma instancia de uma classe
# O que é um atributo? É uma caracteristica do objeto
# O que é um metodo? É um comportamento do objeto
# O que é uma instancia? É um objeto criado a partir de uma classe
# O que é um construtor? É um metodo especial usado para criar objetos
# O que é o self? É uma referencia a instancia atual da classe
# O que é o __init__? É um metodo construtor que é chamado quando um objeto é criado
# O que é o __str__? É um metodo que retorna uma representação em string do objeto
# O que é o __dict__? É um dicionario que contem os atributos do objeto
# O que é o __doc__? É uma string que contem a documentação da classe
# O que é o __name__? É uma string que contem o nome do modulo
# O que é o __module__? É uma string que contem o nome do modulo que define a classe
# O que é o __bases__? É uma tupla que contem as classes base
# O que é o __class__? É uma referencia a classe do objeto
# O que é o __del__? É um metodo chamado quando o objeto é destruido
# O que é o __call__? É um metodo chamado quando o objeto é chamado como uma função
# O que é o __len__? É um metodo chamado quando a função len() é chamada para o objeto
# O que é o __getitem__? É um metodo chamado quando o objeto é indexado
# O que é o __setitem__? É um metodo chamado quando o objeto é atribuido
# O que é o __delitem__? É um metodo chamado quando o objeto é deletado
# O que é o __iter__? É um metodo chamado quando o objeto é iterado

# Sintaxe de uma classe
# class nome_da_classe:
#    nome_do_atributo = valor_do_atributo

#    def __init__(self, atributo1, atributo2):
#         self.atributo1 = atributo1
#         self.atributo2 = atributo2

class Estudante:       # Classe, modelo,
    escola = "DIO"     # Variavel de classe ( atributo de classe  e atribuição de valor)

    def __init__(self, nome, matricula): # Metodo construtor
        self.nome = nome                 # Variavel de instancia
        self.matricula = matricula       # Variavel de instancia

    def __str__(self) -> str:            # Metodo especial
        return f"{self.nome} - {self.matricula} - {self.escola}" # Variavel de classe


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
print()

aluno_1 = Estudante("Guilherme", 1) # Criando uma instância na classe e Inserindo valores
aluno_2 = Estudante("Giovanna", 2)  # Criando uma instância na classe e Inserindo valores
mostrar_valores(aluno_1, aluno_2) 
print()  

Estudante.escola = "Python" # Alterando o valor da variavel de classe

aluno_3 = Estudante("Chappie", 3) # Criando uma instância na classe e Inserindo valores
mostrar_valores(aluno_1, aluno_2, aluno_3) # Mostrando os valores
print()

aluno_1.escola = "DIO" # Alterando o valor da variavel de instancia
mostrar_valores(aluno_1, aluno_2, aluno_3) # Mostrando os valores
print()