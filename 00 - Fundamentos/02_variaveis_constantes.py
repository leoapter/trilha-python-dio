# Boas práticas para nomear variáveis e constantes em Python
# Variáveis: snake_case . Nnomear com letras minúsculas e separar palavras com underline
# Constantes: Nomear com letras maiúsculas e separar palavras com underline
# Exemplo: limite_saque_diario, LIMITE_DIARIO, BRAZILIAN_STATES
# Python não tem um tipo de dado específico para constantes, mas é uma convenção de programação
# Usar nomes significativos e sugestivos  para as variáveis e constantes
# Evitar nomes genéricos e siglas
# Evitar acentos e caracteres especiais
# Não usar palavras reservadas do Python
# Não usar espaços em branco no nome das variáveis e constantes
# Não usar números no início do nome das variáveis e constantes
# Não usar caracteres especiais no nome das variáveis e constantes

nome = "Guilherme"
idade = 28

# É possível atribuir novos valores para as variáveis.
# Porém, é uma boa prática manter o mesmo tipo de dado para a variável.
# O Python vai entender que a variável é do tipo do último valor atribuído.
# É permitido atribuir os valores conforme abaixo, porém não é uma boa prática.

nome, idade = "Giovanna", 27 # aqui foi atribuido novos valores para as variáveis nome e idade

print(nome, idade) # Giovanna 27 . Aqui foi impresso os novos valores atribuidos as variáveis nome e idade 


limite_saque_diario = 1000

LIMITE_DIARIO = 1000  # Convenção de constantes em Python. Declarada em caixa alta.
LIMITE_DIARIO = 200   # Mas se tentar alterar o valor de uma constante, o Python não vai reclamar.
print(LIMITE_DIARIO)

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]  # Convenção de constantes em Python. Declarada em caixa alta.

print(BRAZILIAN_STATES)
