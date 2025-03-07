# Método Remove
# Utilizado para retirar um objeto, atraves do nome do objeto.
# Rtira um de cada vez, cujo indice for o menor
# Se precisar retirar mais de um objeto com o mesmo nome na lista, precisará faze-lo novamente
# Uma das possibilidades é utiizar a função count para saber quantas são as ocorrencias e aplicar o remove tantas vezes quanto necessário

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]
