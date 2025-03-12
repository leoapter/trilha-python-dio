# Objetos de Primeira Classe
# Em Python tudo é Objeto
# Em Python funções são Objetos de Primeira Classe
# Com isso podemos atribuir funções às variáveis,
# passá-las como parâmetro para funções,
# usá-las como valores em estrutura de dados,
# tais como listas, tuplas, dicionários, etc...
# e usar como valor de retorno para uma função (closures = )
# Outros Objetos de Primeira Classe: sting, 

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def blablabla(a, b): # È possível atribuir qualquer nome à função
    return(a**2 + b*3) # O que importa é o que essa função retorna

def exibir_resultado(a, b, funcao): # essa função chama outra função. Aqui o atributo função, na verdade é o resultado de outra função
    resultado = funcao(a, b) # a variável "resultado" é o resultado da outra função atribuida 
    print(f"O resultado da operação = {resultado}")

# Aqui a função é chamada, atribuindo "os valores e o nome da função que ela esta chamando"
print()
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(20, 10, subtrair)
exibir_resultado(5, 8, multiplicar)
exibir_resultado(48, 6, dividir)
exibir_resultado(2, 4, blablabla)
#                ^  ^   ^
#               arg arg função
print()

op = somar # estou atribuindo a função somar para a variável op
print(op(5, 10)) # estou atribuindo os valores a e b à função somar e executando a função
print()

op = subtrair
print(op(5, 10))