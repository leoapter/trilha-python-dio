# Estruturas condicionais
# Utilizados para tomada de decisões
# Estrutura básica: if, elif, else
# Operadores de comparação: ==, !=, >, <, >=, <=
# Operadores lógicos: and, or, not
# Operadores de identidade: is, is not
# Operadores de associação: in, not in
# Operadores de membro: &, |, ^, ~, <<, >>
# Operadores de atribuição: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
# Operadores aritméticos: +, -, *, /, %, //, **
# Util

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
IDOSO = 60

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")
# Fim do bloco if
print() # Pula linha. F

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

else:
    print("Ainda não pode tirar a CNH.")
# Fim do bloco if
print() # Pula linha.


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")
# Fim do bloco if
print() # Pula linha.

# Estrutura condicional aninhada
if idade >= IDADE_ESPECIAL:
    if idade == IDADE_ESPECIAL:
        print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
    elif idade >= MAIOR_IDADE and idade < IDOSO:
        print("Maior de idade, pode tirar a CHN.")
    else:
        print("Idoso, precisa renovar a CNH a cada 5 anos.") 
else:
    print("Menor de Idade. Ainda não pode tirar a CNH.")