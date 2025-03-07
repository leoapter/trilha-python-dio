# Estrutura de repetição while
# O while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.
# Faz sentido utilizar o while quando não sabemos quantas vezes um bloco de código deve ser executado.
# O while é composto por uma condição e um bloco de código.
# A condição é avaliada antes da execução do bloco de código.
# Se a condição for verdadeira, o bloco de código é executado.
# Após a execução do bloco de código, a condição é avaliada novamente.

opcao = -1 # Foi inserido um valor diferente de 0 para que o loop seja executado pelo
# menos uma vez, caso contrário, o loop não seria executado
# esse valor é alterado no loop, então, não é necessário declarar a variável novamente
# esse valor é alterado na função input, então, não é necessário declarar a variável novamente

while opcao != 0:
    print()
    opcao = int(input("Para continuar escolha uma das opções abaixo: \n[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao == 0:
        print("Obrigado por usar nossos serviços, até breve!")
    else:
        print("Opção inválida! Tente novamente.")

print()
