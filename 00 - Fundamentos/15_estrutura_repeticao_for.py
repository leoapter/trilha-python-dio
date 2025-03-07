# Estrutura de repetição for
# Utilizado para iterar sobre uma sequência de elementos
# Exemplo: strings, listas, tuplas, dicionários, etc.
# Também pode ser utilizado para iterar sobre um intervalo conhecido de vezes.
# A sintaxe é: for variavel in iterável: A variavel é o elemento atual do iterável

texto = input("Informe um texto: ") # Vamos solicitar um texto ao usuário
# Exemplo: "Python é uma linguagem de programação"
# Vamos imprimir apenas as vogais do texto
# Definindo as vogais
VOGAIS = "AEIOU" # Constante definindo as vogais, para facilitar a leitura do código

# Exemplo utilizando um iterável
for letra in texto: # Itera sobre cada objeto iteravel na veriavel. Neste caso, foi nomeado texto e é uma string.
                    # O indice letra recebe a cada loop, o item que está sendo iterado no texto. 
                    # Poderia ter qualquer nome, que iria funcionar do mesmo jeito.
    if letra.upper() in VOGAIS: # Verifica se o item que foi iterado naquele indice pertence ao conjunto nomeado como vogais. Pertence = True, Não pertence = False
        print(letra, end="") # Se pertencer, imprime o item iterado. O end="" é para não quebrar a linha

print()  # adiciona uma quebra de linha

# Exemplo Estrutura Condicional For,  utilizando a função built-in range
for numero in range(0, 51, 5): # range(inicio, fim, passo) - O range gera uma sequência de números, iniciando em 0, até 51, com passo de 5
    print(numero, end="-") # Imprime o número iterado, com o end="" para não quebrar a linha. O que estiver dentro do loop, será executado a cada iteração
                           # O que estiver dentro das aspas, será impresso na tela (espaço, virgula, simbolo, etc...)