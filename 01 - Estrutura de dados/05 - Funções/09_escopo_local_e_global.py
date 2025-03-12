# Escopo Local e Escopo Global
# Dentro do Bloco, o escopo é local
# As alterações alí feitas em objetos imutáveis, serão perdidas quando o método terminar de ser executado
# Para usar objetos global, utilizamos a palavra-chave global
# A palavra-chave global informa ao interpretador que a variavel que esta sendo maipulada no escopo local é global
# Mas essa NÃO É UMA BOA PRÁTICA e DEVE SER EVITADA

salario = 2000 # Essa é uma variável de Escopo Global,
               # porque está n raiz do peograma e fora da função


def salario_bonus(bonus): # Dentro do Escopo (Bloco) os objetos são mutáveis
    global salario   # aqui foi criada uma variável salario mas sem atribuição de valor interno ao bloco
    salario += bonus # 
    return salario

salario_com_bonus = salario_bonus(500)  # Aqui "chamamos a função", atribuimos um valor ao atributo bonus, criamos uma variável e atribuimos um novo nome 
print(f'O salário com bonus é R$ {salario_com_bonus}')    # 2500
print()

# ESCOPO LOCAL
def salario_bonus(bonus): # Dentro do Escopo (Bloco) os objetos são mutáveis
    salario = 5000  # aqui foi criada uma variável salario, com atribuição de valor interno ao bloco
    salario += bonus # 
    return salario

salario_com_bonus = salario_bonus(200)  # Aqui "chamamos a função", atribuimos um valor ao atributo bonus, criamos uma variável e atribuimos um novo nome 
print(f'O salário com bonus é R$ {salario_com_bonus}')    # 5.200


