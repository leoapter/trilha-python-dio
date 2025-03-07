# Método Copy
# Utilizado para copiar e criar uma nova lista em uma instancia diferente

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)         # [1, "Python", [40, 30, 20]]
print(lista.copy())  # [1, "Python", [40, 30, 20]]
print()
l2 = lista.copy()    # Atribui o nome l2 para a cópia da lista

print(id(l2), id(lista)) # Os Id's são diferentes = Instancias/Objetos diferentes
print()