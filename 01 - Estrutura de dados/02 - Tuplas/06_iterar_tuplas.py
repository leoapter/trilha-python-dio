# Iteração em tuplas
# Utiliza a função FOR
# Para iterar e saber o valor do indice utilizamod o enumerate


carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)
print()

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
