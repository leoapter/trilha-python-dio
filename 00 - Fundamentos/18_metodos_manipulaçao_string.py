nome = "pYtHon"  #  String com letras maiúsculas e minúsculas

# Métodos de transformação de strings
print(nome) # Imprime a string original
print(nome.upper()) # Transforma todas as letras em maiúsculas
print(nome.lower()) # Transforma todas as letras em minúsculas
print(nome.title()) # Transforma a primeira letra de cada palavra em maiúscula
print(nome.capitalize()) # Transforma a primeira letra da primeira palavra em maiúscula
print()

texto = "  Olá mundo bom demais!    "
print(texto)         # Imprime a string original
print(texto + ".")   # Adiciona um ponto (ou qualquer caractere) ao final da string
print()

# Métodos de remoção de espaços em branco
print(texto.strip())     # Remove os espaços em branco do início e do final da string
                         # O método strip() não remove espaços em branco entre as palavras
                         # Para remover espaços em branco entre as palavras, utilize o método replace()
print(texto.replace(" ", ""))  # Remove os espaços em branco entre as palavras
print(texto.rstrip())    # Remove os espaços em branco à direita do final da string
print(texto.lstrip())    # Remove os espaços em branco à esquerda do início da string
print()                  # Imprime uma linha em branco

menu = "Python é tudo"

# Metodo que centraliza e adiciona caracteres à esquerda e à direita da string
print("#####" + menu + "#####")  # Adiciona caracteres à esquerda e à direita da string
print(menu.center(22))         # Centraliza a string em um espaço de 14 caracteres
print(menu.center(22, "#"))    # Centraliza a string em um espaço de 14 caracteres e adiciona # à esquerda e à direita
print()

# Metodo que justifica e adiciona caracteres à esquerda e à direita da string
print(menu.ljust(22, "-"))     # Justifica a string à esquerda em um espaço de 14 caracteres e adiciona - à direita
print(menu.rjust(22, "-"))     # Justifica a string à direita em um espaço de 14 caracteres e adiciona - à esquerda
print()

# Método que divide a string em uma lista de substrings
print(menu.split())           # Transforma  a string em uma lista de substrings
print(menu.split("t"))        # Divide e Transforma a string em uma lista de substrings a partir do caractere "t"
print(menu.split("t", 1))     # Divide e Transforma a string em uma lista de substrings a partir do caractere "t" e limita a 1 ocorrência
print(menu.split("t", 2))     # Divide e Transforma a string em uma lista de substrings a partir do caractere "t" e limita a 2 ocorrências
print(type(menu.split("t", 2)))      # Verifica o tipo de dado retornado pelo método split()
print()

print("-".join(menu))      # Adiciona - entre cada caractere da string
print()
