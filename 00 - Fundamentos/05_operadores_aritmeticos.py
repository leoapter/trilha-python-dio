produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)  # soma
print(produto_1 - produto_2)  # subtração
print(produto_1 / produto_2)  # divisão real, resultado é um float
print(produto_1 // produto_2) # divisão inteira
print(produto_1 * produto_2)  # multiplicação
print(produto_1 % produto_2)  # resto da divisão
print(produto_1 ** produto_2) # exponenciação

# Ordem de precedência (PEMDAS)
# P - Parênteses, E - Expoentes, M - Multiplicação, D - Divisão, A - Adição, S - Subtração
# Exemplo
x = (10 + 5) * 4 # Ordem de precedência (10 + 5) = 15 * 4 = 60
y = (10 / 2) + 25 * ((2 - 2) ** 2) # Ordem de precedência (2 - 2) = 0 ** 2 = 0 * 25 = 0 + 5.0 = 5.0S
print(x)
print(y)
