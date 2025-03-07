# Método Extend
# Utilizado para adicionar novos elementos na lista, utilizando uma outra lista
# Juntar 2 listas
# Ao juntar 2 listas, não exclui valores duplicados

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

linguagens.extend(["js", "java"])

print(linguagens) # ['python', 'js', 'c', 'java', 'csharp', 'js', 'java']
