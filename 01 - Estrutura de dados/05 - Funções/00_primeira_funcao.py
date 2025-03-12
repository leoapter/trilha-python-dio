# Função
# É um bloco de código identificado por um nome 
# Pode receber uma lista de parâmetros
# Os parâmetros podem ou não ter valores
# Torna o código mais legivel
# possibilita o reaproveitamento de código
# programar usando funções = programar de maneira estruturada
# def é uma palvra reservada para o interpretador Python saber que o que vem a seguir é uma função
# DECLARAÇÃO DE FUNÇÃO: sintaxe: def identificador_da_funcao(parametro):
# o que estiver a partir do ":" e estiver indentado abaixo da declaração, faz parte do bloco da função
# ATENÇÃO: Não basta declarar uma função, ela não tem utilidade se não for chamada/executada
# PARA EXECUTAR UMA FUNÇÃO: 
# 1- É necessário "chamar a função" pelo seu identificador_de_funçao
# 2- Se ela não tem argumentos, deixamos os () "vazios"
# 3- Se ela tem argumentos, preciso declarar esses argumetos ao chamar a função



def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome): # Se foi declarado um argumento sem valor, o mesmo precisa ser fornecido na execução da função
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # Se foi declarado um aargumento com valor, este valor é considerado default, mas pode ser substituido na execução da função
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()                    # Olá mundo!
exibir_mensagem_2(nome="Guilherme")  # Seja bem vindo Guilherme!
exibir_mensagem_3()                  # Seja bem vindo Anônimo!
exibir_mensagem_3(nome="Chappie")    # Seja bem vindo Chappie!
