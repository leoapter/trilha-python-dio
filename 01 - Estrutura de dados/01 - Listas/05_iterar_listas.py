# Iterar uma lista
# Causa a extração dos valores de uma lista

carros = ["gol", "celta", "palio"]

for carro in carros: # Pode itilizar qualquer nome para o iterável. Não muda nada
    print(carro)
# gol
# celta
# palio
print()

for carro in carros: # carro é o nome do iterador e carros é o iteravel na lista
    print(carro, end = " ") # gol celta palio
print()
print()

# Muitas vezes precisamos conhecer o indice de valores iterados de uma lista
# A função enumerate faz isso
# O iterador e o iterável devem ser utilizados na função enumerate
for indice, carro in enumerate(carros): # enumera os indices lado a lado dos valores iterados
    print(f"{indice}: {carro}")
print()    

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}", end = ", ")
print()
print()