# Convertendo e Formatando datas e horas - usando mascaras
# Metodo strftime (string format time) 
# Método strptime (string parse time)
# ATENÇÃO timedelta NÃO TRABALHA com formato string
# Para fazer calculos com data e hora é necessário converter uma string para o formato datetime
# Para converter string para datetime use a função strptime

from datetime import datetime
print()
d = datetime.now()
# Formatando data e hora usando máscara
print(d.strftime('%d/%m/%Y %H:%M')) # 08/03/2025 20:12
print()

# Convertendo a data formato string para datetime, usando strptime
date_string = "08/03/2025 20:17" # Não é possivel fazer caldulos com string
# ATENÇÃO: a mascara utilizada na função strptime deve ser a mesma
# da utilizada na data_formato_string, senão vai dar erro...
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M") # Convertendo str para datetime
print(d)
print()

data_hora_atual = datetime.now()
data_hora_str = "2025-03-08 20:26"
print(data_hora_str)
print(type(data_hora_str))

# Criando a mascara ptbr
# O "a" significa que a saida será o dia da semana abreviada e "A" por extenso. 
mascara_ptbr = "%d/%m/%Y %a"
# Criando a mascara en
mascara_en = "%Y-%m-%d %H:%M"

# Imprimindo em formato string
print(data_hora_atual.strftime(mascara_ptbr))
print(type(data_hora_atual.strftime(mascara_ptbr)))
print()

# Imprimindo em fotmato datetime
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))
print()
