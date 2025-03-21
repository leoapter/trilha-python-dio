# Propriedades
# A propriedade @property que envolve uma função, tem a propriedade de transformar valores de atribuição que podem ser reutilizados em saidas e/ou cálculos
# Se não se pretende fazer calculos com os valores de atribuição, não tem sentido utilizar propriedades

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
        print(nome)
        print(ano_nascimento)
        print(f'Nome:{nome}, Ano de nascimento: {ano_nascimento}')

    @property  # aqui definimos uma propriedade computada, que lê o ano de nascimento e calcule a idade
               # se a propriedade @property não for declarada, o calculo não vai funcionar
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento


pessoa1 = Pessoa("Guilherme", 1994) # Instanciando a instância Pessoa 
print(f"Nome: {pessoa1.nome} \tIdade: {pessoa1.idade}")

pessoa2 = Pessoa("Leo Apter", 1956)
print(f'Nome: {pessoa2.nome} \tIdade: {pessoa2.idade}')
