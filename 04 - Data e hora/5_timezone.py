# Modulo timezone do python
# Se o pytz não estiver funcionando ou dando conflito usar esse mesmo


from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))
data_tel_aviv = datetime.now(timezone(timedelta(hours=2)))
data_nova_york = datetime.now(timezone(timedelta(hours=-5)))

print()
print(data_oslo)
print()
print(data_sao_paulo)
print()
print(data_tel_aviv)
print()
print(data_nova_york)
print()