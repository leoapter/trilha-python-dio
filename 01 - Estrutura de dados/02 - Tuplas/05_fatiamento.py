# Fatiamento
# Usamos fatiamento quando queremos extrair um conjunto de valores em uma sequencia
# Pode utilizar o indice inicial, indice final, passo, ou uma combinação destes
# [START:STOP:STEP]
# É diferente do acesso direto onde conseguimos extrir apenas um valor por vez


tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")
print()

print(tupla[0], [2], [5]) # acesso direto funciona mas dá erro na saida --> p [2] [5]
print()

print(tupla[0]) # acesso direto     p  
print(tupla[2]) # acesso direto     t
print(tupla[5]) # acesso direto     b