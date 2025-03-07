# Método Index
# Utilizado para saber qual é primeira ocorrencia de um determinado objeto
# Se houver repetições, vai retornar apenas a 1a ocorrncia

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
print()

linguagens = ["python", "java", "js", "c", "java", "csharp", "java", "html"]
print(linguagens.index("java")) # 1
print()