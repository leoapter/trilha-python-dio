# Operadores lógicos são utilizados para fazer comparações entre expressões
# São utiizados em conjunto com operadores de comparação.
# True = 1, False = 0
# Tem a função de verificar se uma ou mais expressões são verdadeiras
# and = para ser True tudo tem que ser True. Formula matemática: 1 * 1 = 1, 1 * 0 = 0
# or = para ser True apenas um tem que ser True. Formula matemática: 1 + 1 = 1, 1 + 0 = 1
# not = inverte o valor da expressão. Formula matemática: 1 = 0, 0 = 1

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)
print()
saldo = 1000
saque = 250
limite = 200
conta_especial = True
print()

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # Expressão matemática = 1 * 0 + 1 * 1 = 1 . Legibiiidade ruim
print(exp)
print()

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # Expressão matemática = (1 * 0) + (1 * 1) = 1 . Legibiiidade boa
print(exp_2)
print()

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite # Expressão matemática = 1 * 0 = 0
print(conta_normal_com_saldo_suficiente)
print()

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque # Expressão matemática = 1 * 1 = 1
print(conta_especial_com_saldo_suficiente)
print()

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente # Expressão matemática = 0 + 1 = 1
print(exp_3)
print()
