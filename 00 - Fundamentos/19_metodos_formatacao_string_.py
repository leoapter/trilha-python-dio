# Metodos de manipulação de string

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

# Metodo Old Style. Pouco utilizado , pode ser confuso e dificil de manter
print("Nome: %s Idade: %d" % (nome, idade)) # %s = string, %d = inteiro, %f = float
print()

# Metodo Format.Não tem muita diferença do Old Style, mas é mais legivel
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print()
# Metodo Format com dicionario
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
print()

# Metodo Formatação com fstring. Recomendado, por ser mais legivel e facil de manter
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
print()

PI = 3.14159265359
print(PI)
print(f"PI: {PI}") # Sem formatação
print(f"PI: {PI:.2f}") # Função round. Arredonda o valor para 2 casas decimais
print(f"PI: {PI:.3f}") # Função round. Arredonda o valor para 3 casas decimais
print(f"PI: {PI:10.2f}") # Função round. Arredonda o valor para 2 casas decimais e adiciona 10 espaços a esquerda
print()

print(f'Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}, Saldo: {saldo:.2f}') # A função round arredonda o valor para 2 casas decimais
print(f'Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem.upper()}')
print(f'Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem.lower()}')
print(f'Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem.capitalize()}')
