# Fatiamento
# O Fatiamento cria uma nova lista ou uma cópia da lista

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"] . Vai da posição 2 até o final da lista
print(lista[:2])  # ["p", "y"] . Vai da posição 0 até a posição 1 (2-1)
print(lista[1:3])  # ["y", "t"] . Vai da posição 1 até a posição 2 (3-1)
print(lista[0:3:2])  # ["p", "t"] . Vai da 0 até a 2 (3-1), de 2 em 2
print(lista[::])  # ["p", "y", "t", "h", "o", "n"] . Pega a lista toda
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"] . Espelha a lista
