# Listas aninhadas ou matriz
# Abaixo temos uma matriz bidimensional 3 x 3
# Para melhor visualização, recomenda-se colocar cada lista aninhada em uma linha abaixo da outra

matriz = [
    [1, "a", 2], # linha 0
    ["b", 3, 4], # linha 1
    [6, 5, "c"]  # linha 2
]

print(matriz[0])  # [1, "a", 2] . Pega toda linha 0
print(matriz[0][0])  # 1 . Pega e intersecção da linha 0 e coluna 0
print(matriz[0][-1])  # 2 . Pega a intersecção da linha 0 e a ultima coluna
print(matriz[-1][-1])  # "c" . Pega a intersecção da ultima linha e ultima coluna
print(matriz[2][2])  # "c" . Intersecção da 3a linha e 3a coluna
print(matriz[1][1])  # 3
print(matriz[1][2])  # 4
# print(matriz[3][3])  # erro. está fora da limite da matriz