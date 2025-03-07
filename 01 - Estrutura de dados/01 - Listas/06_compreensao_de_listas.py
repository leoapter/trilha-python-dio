# Compreention ou Compreensão
# Usado para criar uma nova lista ou modificar a existente utilizando uma lista existente

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]

# Maneira 1
pares = [] # Nome da função ond vou armazenar os meus dados
for numero in numeros:
    if numero % 2 == 0: # Essa equação verifica se o iteravel é um numero par (divisão por 2 com resto = 0)
        pares.append(numero) # O append insere os valores na lista indicada "pares"
print(pares)
print()

# Metodo Compreention, com sintaxe mais simples e melhor compreensão

# Com filtro
# No exemplo da função a seguir, verifica quais são os numeros pares e cria uma nova lista com estes numeros
pares = [numero for numero in numeros if numero % 2 == 0] # Leitura: Faça uma nova lista utilizando o(s) numero(s) da lista numeros, se o numero for par
print(pares)
print()

# Sem filtro
# Modificar valores
# No exemplo a seguir cria uma nova lista com valores exponencializados da original
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros] # Leitura: Faça uma nova lista, elevando ao quadraro, todos os numeros na lista numeros
print(quadrado)
print()
