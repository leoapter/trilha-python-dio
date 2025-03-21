# Herança Múltipla
# class A:
#   pass
# class B(A):
#   pass
# class C(A, B):
#   pass

# MRO: Method Resolution Order
# Django?

class Animal:                        # Criando a classe "Animal"
    def __init__(self, nro_patas):   # Incializando a classe e definindo os atributos da classe (self, nro_patas)
        self.nro_patas = nro_patas   # Definindo a atribuição do atributo da classe. Atributo da Classe = Atribuição

    def __str__(self):               # 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  # 


class Mamifero(Animal):                 # Criando a Classe "Mamifero", Subclasse/Extensão/filha de 'Animal"
    def __init__(self, cor_pelo, **kw): # Incializando a classe e definindo os atributos da classe (self, cor_pelo), determinando que  que está à esquerda seja kwargs ( key = arg), ouseja, chave = argumeto/nome.
        self.cor_pelo = cor_pelo        # Atributo de casse = Atribuição. ATENÇÃO: Quando trabalhamos com herança, declaramos na sub-classe APENAS os atributos que são exclusivos à essa sub-classe. 
        super().__init__(**kw)          # Inicializando uma superclasse em forma de dicionario ( chave = valor), para chamar o construtor "pai".
                                        # Desta forma, todos os argumentos definidos na classe pai, poderão ser acessados na classe filha 
                                        # ATENÇÃO: Para isso funcionar, TODOS os atributos da classe filha que são comuns à classe pai, devem ser ATRIBUIDOS DIRETAMENTE na CLASSE PAI, senão vai dar erro...

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero): # Quando na sub-sub classe não existe um comportaménto novo, nenhum método adicional é acrescentado. 
    pass              # Neste caso, é acrescentada a palavra reservada pass. É boa pratica quando definir uma classe, inserir o pass até que sejam criados os seus comportamentos


class Ornitorrinco(Mamifero, Ave):      # Criando  a Herança Múltipla
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato1 = Gato(nro_patas=4, cor_pelo="Preto") # Chamando a instância Gato, dando um nome para essa instância e atribuindo comportamento às suas características (nro_patas e cor_pelo)
                                            # Como o argumento nro_patas foi herdado atravez de **kw, a atribuição do comportamete precisa ser necessáriamente fornecida em chave = valor 
print(gato1)
                                            
gato2 = Gato("Preto e Branco ", nro_patas=4) # Chamando a instância Gato, dando um nome para essa instância e atribuindo comportamento às suas características (nro_patas e cor_pelo)
print(gato2)                                 # Uma outra opção é declarar o comportamento definido na classe como positional, em primeiro lugar, em sua ordem positional, e depois declarar os outros comportamento no formato **kw

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
