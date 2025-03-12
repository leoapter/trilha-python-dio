# Parâmetros Especiais
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
# Tudo o que está atraz da / , está forçado como positional

def criar_carro(modelo, ano, placa, marca, motor, combustivel, /,): # tudo que está atraz da / está forçado positional
    print(modelo, ano, placa, marca, motor, combustivel)
    print()


# Declaração válida. Tudo foi declarado positional.
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # Palio 1999 ABC-1234 Fiat 1.0 Gasolina

# Declaração inválida. Tem parte declarada como keyword (chave=valor), onde está forçado
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # TypeError: criar_carro() got some positional-only arguments passed as keyword arguments: 'marca, motor, combustivel'

# Declaração inválida, Foi declarado keyword (kargs --> chave=valor), onde está forcado positional
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # TypeError: criar_carro() got some positional-only arguments passed as keyword arguments: 'modelo, ano, placa, marca, motor, combustivel'  