# Matriz de tuplas é uma sequencia de tuplas dentro de uma tupla
# É uma boa pratica transforma a sequencia de tuplas em matriz para melhor visualização
# Quando usar tuplas ao invez de lista?
# Quando queremos ter certeza que os valores não poderão ser alterados
# 

matriz = ((1, "a", 2), ("b", 3, 4), (6, 5, "c"),)
print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
print()

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
print()