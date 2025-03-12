# Declarando Tuplas
# class tuple
# É uma estrutura imutável. 
# Não é possível alterar os valores até o final da função
# A sintaxe é: nome_da_tupla = (a , b, c, d,)
# É uma BOA PRÁTICA colocar uma VIRGULA APÓS O ULTIMO ELEMENTO, PRINCIPALMENTE quando houver um único elemento. 
# Outra forma de declarar é nome_da_tupla = tuple(a , b, c, d) 

fruta = ('maçã', 'abacaxi', 'limão')  # Aqui a função foi construida sem a virgula após o ultimo elemento
                                      # Apesar disso o interpretador do Python reconhece como class tuple
print(fruta)                          # ('maçã', 'abacaxi', 'limão')
print(type(fruta))                    # <class 'tuple'>
print()                               


frutas = ("laranja","pera","uva",)  # Aqui a função foi construida com uma virgula após o ultimo elemento        
print(frutas)                       # Desta forma o interpretador do Python reconhece como class tuple
print(type(frutas))                 # <class 'tuple'>
print()                             # ('laranja', 'pera', 'uva')      

frutas = (                          
    "laranja",
    "pera",
    "uva",
)
print(frutas)                     # ('laranja', 'pera', 'uva')
print()

letras = tuple("python")           # Aqui a função transforma string em tuple
print(letras)                      # ('p', 'y', 't', 'h', 'o', 'n')
print(type(letras))                # <class 'tuple'>
print()                            

numeros = tuple([1, 2, 3, 4])      # tupla contendo uma lista, transforma a lista em tupla
print(numeros)                     # (1, 2, 3, 4)
print(type(numeros))               # Uma vez que a lista foi modificada para tupla, os valores aa mesma não poderão ser modificados
print()

pais  = ("Brasil",)          # Aqui a função foi construida COM uma virgula após o ultimo elemento        
print(pais)                  
print(type(pais))            # Desta forma o interpretador do Python reconhece como class tuple
print()                      # ('Brasil',)

pais  = ("Brasil")           # Aqui a função foi construida SEM uma virgula após o ultimo elemento
                             # Desta forma o interpretador do Python reconhece como class sting
print(pais)                  # Brasil
print(type(pais))            # <class 'str'>
print()            


numeros = [1, 2, 3, 4]
print(numeros)
print(type(numeros))
print()

numeros = tuple([1, 2, 3, 4])
print(numeros)
print(type(numeros))
print()