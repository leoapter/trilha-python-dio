# Propriedades: property()
# Com o property() é poível criar atributos gerenciados em suas classes
# Atributos gerenciados são atributos que possuem métodos de acesso, modificação e deleção
# É possível criar atributos somente leitura, somente escrita e somente deleção
# Atributos somente leitura são atributos que não podem ser modificados. @property cria read only. Para poder alterar (settar), é necessário criar  função @setter
# Atributos somente escrita são atributos podem ser modificado @setter cria 
# Atributos somente deleção são atributos que podem ser deletados
# Pode-se usar o property() como decorador
# O property() é um built-in do Python
# Pode usar atributos gerenciados quando precisar de controle sobre o acesso aos atributos de uma classe
# Pode-se usar o property() para criar atributos privados
# O property() é uma forma de encapsulamento
# O property() é uma forma de proteger seus atributos
# Pode ser usado quando precisar modificar a implementação interna, sem alterar a API pública da classe
# Sintaxe:

class Foo:
    def __init__(self, x=None):    
        self._x = x   # atributo e variável privado

    @property  # decorador(envolve uma função). é uma função que executa antes da função seguinte. Transforma o resultado de uma função em atributo
    def x(self):             # função que será executada. Com isso, o atributo x, passa a ser um atributo gerenciado e já fica disponível na classe
        return self._x or 0  # retorna o valor como um atributo privado

    @x.setter  # decorador para setar/modificar um valor
    def x(self, value):      # o self recebe 2 valores. O primeiro é o nome da instância e o segundo (value) é o valor que será modificado
        self._x += value     # aqui é feita a operação

    @x.deleter # decorador para deletar um valor
    def x(self):           # função que será executada
        self._x = 0        # atributo privado recebe 0


foo = Foo(10) # x = 10 (atributo privado). Aqui estamos instanciando o objeto foo, na classe Foo e atribuindo o valor x=10 dentro do @property def x(self)
print(foo.x)  # x = 10 (atributo privado). Aqui estamos acessando a variável .x definidaa na @property, criada logo após a classe Foo, com sintaxe de atributo.
del foo.x     # x = 0 (atributo privado). Aqui estamos deletando o valor de x
print(foo.x)  # x = 0 (atributo privado)
foo.x = 30    # x = 30 (atributo privado). Aqui estamos settando o valor 30 à x
print(foo.x)  # x = 30 (atributo privado)
del foo.x     # x = 0 (atributo privado)
print(foo.x)  # x = 0 (atributo privado)
foo.x = 40    # x = 40 (atributo privado)
print(foo.x)  # x = 40 (atributo privado)
foo.x = 50    # x = 90 (atributo privado)
print(foo.x)  # x = 90 (atributo privado)
foo.x += 5    # x = 185 (atributo privado). Aqui estamos somando 5 ao valor 90 e somando aos valor 90 anterior
print(foo.x)  # x = 185 (atributo privado)