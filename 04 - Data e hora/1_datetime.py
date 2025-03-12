# Módulo datetime
# Utilizado para maipulações precisas de data e hora
# Sintaxe date(y, m, d)


from datetime import date, datetime, time # Importando o módulo datetime

# DATE
data = date(2023, 7, 10) # Calcula apenas a data 
print(data)              # 2023-07-10
print()
print(date.today())      # Imprime a data de hoje (2025-03-07), no formato yyyy-mm-dd

# DATETIME
data_hora = datetime(2023, 7, 10) # calcula a data e a hora. MÉTODO MAIS USADO COMERCIALMENTE
print(data_hora)                  # 2023-07-10 00:00:00
data_hora = datetime(2025,3,7,9,20,34) # informando (y,m,d,h,m,s)
print(data_hora)                  # 2025-03-07 09:20:34
print()
print(datetime.today())    # Imprime a data e horario completo de hoje,no local de execução do programa: 2025-03-07 14:45:21.453177
print(datetime.now())      # Imprime a data e horario completo de agora,no local de execução do programa 2025-03-07 14:45:21.453177
#print(datetime.now(tz=timezone.utc))    # Imprime a data e horario completo de agora,na zona UTC especificada: 2025-03-07 14:45:21.453177
print()

# TIME
hora = time(10, 20, 0)     # calcula apenas a hora, no formato hh:mm:ss
print(hora)                # 10:20:00
print(time)                # mostra a classe <class 'datetime.time'>
