# Retorno de Função
# Para retornar o valor de uma função usamos a palavra reservada "return"
# Toda função Python retorna None por padrão
# Se não houver um valor explicito à retornar, vai retornar None
# Se houver um valor explicito, vai retornar esse valor
# O Python pode retornar mais de um valor
#

def calcular_total(numeros): 
    return sum(numeros)    # A função retorna apenar um valor


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor # # Aqui a função retorna 2 valores


print(calcular_total([10, 20, 34]))  # 64
print(type([10, 20, 34]))  # <class 'list'>
print()

print(retorna_antecessor_e_sucessor(10))  # (9, 11) 
print(type(retorna_antecessor_e_sucessor(10))) # <class 'tuple'>
print()

def func_3():
    print('Olá Mundo!') # Olá Mundo! ---- Não fez parte da função
    return

print(func_3()) # None 