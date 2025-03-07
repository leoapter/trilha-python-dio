# Operadores de associação
# São utilizados para verificar se um valor ou variável está presente em uma sequência	
# in: Retorna True se o valor ou variável está presente na sequência
# not in: Retorna True se o valor ou variável não está presente na sequência

frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas)
print("laranja" in frutas)
print("limao" in frutas)
print()
print("Python" in curso) # False, porque a palavra está com a primeira letra maiúscula
print("Python" not in curso) # True, porque a palavra está com a primeira letra maiúscula
print()
print("python" not in curso) # False, porque a palavra está com a primeira letra minúscula
print("python" in curso) # True, porque a palavra está com a primeira letra minúscula
