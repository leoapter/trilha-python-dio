# args e kwargs
# Podemos combinar parâmetros obrigatórios com args e kwargs
# *args: O método recebe os valores como tupla
# **kwargs: O metodo recebe os valores como dicionário
# Dicionário precisa ter chave : valor (com 2 pontos) 


def exibir_poema(data_extenso, *args, **kwargs): # Aqui ficam definidos os argumentos. O primeiro esta por posicionamento, a seguir *(tuplas) e finalmente **(dicionário)
    #                                            # Foi atribuido o valor data_extenso para o primeiro argumento. Podia ser qualquer outro nome e/ou conteudo na sequencia
                                                 # Para os argumentos seguintes foi informado que eram tuplas e os ultimos dicionário
    texto = "\n".join(args)    # aqui pede para juntar as tuplas e imprimir cada argumento em outra linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # significa para chave e valor no dicionario junte e imprima chave: valor pulando a linha
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # concatene o primeiro argumento, pule 2 linhas, iconcatene os args, pule 2 linhas e concatene os args
    print(mensagem)  # imprima conforme instrucao acima
# É difícil de perceber, mas o poema esta escrito como uma sequencia
# Inicia em formato tupla (str, str, str...)
# No final muda para dicionário ( ...str, str, chave=valor, chave=valor, )
# inclusive com uma vírgula após o ultimo argumento...

exibir_poema(
    "Domingo, 09 de março de 2025",               
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
