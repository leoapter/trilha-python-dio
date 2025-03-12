# Manipulação de dadas e horas
# timedelta

from datetime import date, datetime, timedelta

# Criando data e hora
d = datetime(2025, 3, 7, 17, 52)
print(d)

# Adicionando 1 semana
d = d + timedelta(weeks=1)
print(d)
print()

# Lava-rápido
tipo_carro = "G"  # P, M, G
tempo_pequeno = 30 # minutes
tempo_medio = 45   #
tempo_grande = 60  #
data_atual = datetime.now() # pega data e hora de hoje, no momento em que a função for chamada
                            # pode usar o utcnow()
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

# Não é possível utilizar a mesma metodologia para calcular horas
# Para isso, é necessário é fazer o calculo
# E em seguida extratir o resultado no formato time.
# Desta forma a data será ignorada e a saida será apenas hora
# ATENÇÃO timedelta NÃO TRABALHA com formato string

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

# Para obter apenas hora, extrair saida do datetime no formato date
print(datetime.now().date())