# Módulo pytz
# Esse módulo permite trabalhar com Fuzo Horário Time-zome
# É um módulo externo do Python
# È necessário instalar o pytz pelo terminal antes de importar 
# É necessário importat o datetime do datetime e o pytz. comando pip install pytz

from datetime import datetime

import pytz # esta dando erro. está dando conflito precisa usar outro interpretador

# Criando datetime com timezone
data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)
