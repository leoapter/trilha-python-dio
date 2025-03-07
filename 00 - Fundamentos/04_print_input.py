# Função Input e Print

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade) # O print() aceita mais de um argumento.
print(nome, idade, end="...\n") # Adiciona um caractere ao final da string e pula uma linha.
print(nome, idade, sep="#", end="...\n") # Adiciona um caractere entre os argumentos e ao final da string e pula uma linha.
print(nome, idade, sep="#") # Adiciona um caractere entre os argumentos.
print(nome, idade, sep="#", end="...") #Adiciona um caractere entre os argumentos e ao final da string, mas não pula uma linha.
print(nome, end = "")  # Adiciona um caractere ao final da string, mas não pula uma linha.)
print(idade) # Vai ficar colado com o print anterior, pois não foi adicionado um caractere ao final da string.