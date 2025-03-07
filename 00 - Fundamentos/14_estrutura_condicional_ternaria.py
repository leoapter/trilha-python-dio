# Estrutura condicional ternária
# É utilizada para simplificar a escrita de estruturas condicionais compostas. 
# È composta por três partes: a condição, o resultado se a condição for verdadeira e o resultado se a condição for falsa.
# Sintaxe: condição_verdadeira if condição else condição_falsa
# Exemplo: status = "Sucesso" if saldo >= saque else "Falha", onde status é a variável que receberá o resultado da condição, saldo é a variável que será comparada com saque e saque é a variável que será comparada com saldo.
# O resultado da condição será armazenado na variável status.
# É utilizada para simplificar a escrita de estruturas condicionais compostas. 
# É utilizada para uma verificação simples, onde a condição é simples e o resultado é simples.
# Não é recomendada para estruturas condicionais complexas, pois a leitura do código pode ficar prejudicada.

saldo = 2000
saque = 1500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
