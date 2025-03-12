# Argumentos Nomeados
# Argumento pode ser informados de 3 maneiras
# 1- Informando o argumento em ordem sequencial (positional)
# 2- Informando o argumento na forma de nome_de_chave = valor (keyword)
# No caso 1 e/ou 2, quando chamar a função é obrigatório respeitar a ordem e/ou os nome_de_chave
# 3 - Dicionário
# Quando a declaração da função não é forçada (parâmetros especiais --> inserido os simbolos "/" ou "*", ) 
# # pode-se inserir os argumentos de forma livre


def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # argumento posicional
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # argumento keyword (chave = valor)
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # simbolo ** no inicio -->dicionário
