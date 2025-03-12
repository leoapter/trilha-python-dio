# Parâmetros Especiais
# Utilizam os simbolos "/" e/ou "*"
# Por padrão argumentos podem ser passados por:
# Posição
# Nome (explicitamente)
# Hibrido
# Para melhor vivibilidade e desempenho faz sentido restringir
# a maneira pelo qual os orgumentos possam ser passados
# O desenvolvedor precisa apenas olhar para a definição da função para determinar
# se os itens são passados por posição, por posição e nome, ou por nome
# Podemos forçar isso
# Sintaxe: def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#                ==========     ==========     ==========
# positional only ^    positional or keyword     ^ keyword only
# Tudo o que está atraz do simbolo / está forçado como positional
# Tudo o que está após o simbolo * está forçado como keyword

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#         tudo o que está atraz da  ^ forçando positional only, Após isso pode ser positional or keyword
    print(modelo, ano, placa, marca, motor, combustivel)

# Declaração válida
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
print()

# Declaração válida, Foi declarado positional, onde está forcado hibrido positional ou keyword
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
print()

# Declaração inválida, Foi declarado keyword (kargs --> chave=valor), onde está forcado positional
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # TypeError: criar_carro() got some positional-only arguments passed as keyword arguments: 'modelo, ano, placa'
