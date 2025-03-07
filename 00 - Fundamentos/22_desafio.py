menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""  # Essa formatação permite atualizar a variavel extrato com uma string cumulativa, 
              #linha à linha, a cada interação, sem sobreescrever a anterior.
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor # Essa linha é responsável por atualizar a variavel "saldo" na função principal
            extrato += f"Depósito: R$ {valor:.2f}\n" # Essa linha é responsável por atualizar a variavel "extrato" na função principal
                                                     # O \n é para pular uma linha após a inserção da transação

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor   # Essa linha é responsável por atualizar a variavel "saldo" na função principal
            extrato += f"Saque: R$ {valor:.2f}\n" # Essa linha é responsável por atualizar a variavel "extrato" na função principal
                                                  # O \n é para pular uma linha após a inserção da transação

            numero_saques += 1 # # Essa linha é responsável por atualizar a variavel "numero_saques" na função principal

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
