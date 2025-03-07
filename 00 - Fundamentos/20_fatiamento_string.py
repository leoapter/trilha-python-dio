# Método Fatiamento de String

nome = "Guilherme Arthur de Carvalho"

print(nome[0])        # Retorna o primeiro caractere da string: G
print(nome[1])        # Retorna o segundo caractere da string: u
print(nome[-2])       # Retorna o penúltimo caractere da string: h
print(nome[-1])       # Retorna o último caractere da string: o
print(nome[:9])       # Retorna os 9 primeiros caracteres da string: Guilherme
print(nome[10:])      # Retorna os caracteres a partir do 10º caractere da string: Arthur de Carvalho
print(nome[10:16])    # Retorna os caracteres do 10º ao 16º caractere da string: Arthur
print(nome[10:16:2])  # Retorna os caracteres do 10º ao 16º caractere da string pulando de 2 em 2: Aru
print(nome[::2])      # Retorna todos os caracteres da string pulando de 2 em 2: GieeAtrd aalh
print(nome[:])        # Retorna todos os caracteres da string: Guilherme Arthur de Carvalho
print(nome[::-1])     # Retorna todos os caracteres da string de trás para frente (inverte a sequencia): ohlavraC ed ruhtrA emrehliuG
