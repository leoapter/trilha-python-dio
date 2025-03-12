# Propriedades: property()
# Com o property() é poível criar atributos gerenciados em suas classes
# Atributos gerenciados são atributos que possuem métodos de acesso, modificação e deleção
# É possível criar atributos somente leitura, somente escrita e somente deleção
# Atributos somente leitura são atributos que não podem ser modificados
# Atributos somente escrita são atributos que não podem ser lidos
# Atributos somente deleção são atributos que não podem ser deletados
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
        self._x = x   # atributo privvado

    @property  # decorador. é uma função que executa antes de outra função
    def x(self):             # função que será executada
        return self._x or 0  # retorna o valor do atributo privado

    @x.setter  # decorador para setar/modificar um valor
    def x(self, value):      # value é o valor que será passado
        self._x += value     # aqui é feita a operação

    @x.deleter # decorador para deletar um valor
    def x(self):           # função que será executada
        self._x = 0        # atributo privado recebe 0


foo = Foo(10) # x = 10 (atributo privado)
print(foo.x)  # x = 10 (atributo privado)
del foo.x     # x = 0 (atributo privado)
print(foo.x)  # x = 0 (atributo privado)
foo.x = 30    # x = 30 (atributo privado)
print(foo.x)  # x = 30 (atributo privado)
del foo.x     # x = 0 (atributo privado)
print(foo.x)  # x = 0 (atributo privado)
foo.x = 40    # x = 40 (atributo privado)
print(foo.x)  # x = 40 (atributo privado)
foo.x = 50    # x = 90 (atributo privado)
print(foo.x)  # x = 90 (atributo privado)
foo.x += 5    # x = 185 (atributo privado) ????
print(foo.x)  # x = 185 (atributo privado) ????