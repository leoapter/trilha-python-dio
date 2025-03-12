# Parâmetros somente por nome --> keyword only
# Inicia a sequencia de parâmetros com o *
# Se tentar inserir parametros positionais, dará erro.

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Quando se "chama" uma função, não é necessário a função print para mostrar o resultdo

# Válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Palio 1999 ABC-1234 Fiat 1.0 Gasolina
print()

# Inválido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # TypeError: criar_carro() takes 0 positional arguments but 3 positional arguments (and 3 keyword-only arguments) were given