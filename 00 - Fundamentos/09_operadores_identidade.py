# Operadores de identidade são utilizados para comparar objetos, se são iguais ou não.
# is = é, is not = não é

curso = "Curso de Python"
nome_curso = curso
curso is nome_curso
print(curso is nome_curso)
print()
print(curso is not nome_curso)
print()

saldo = 1000
limite = 1000

print(saldo is limite)
print()
print(saldo is not limite)
print()
