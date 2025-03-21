## Introdução e Conceitos

# Módulo vs Pacote

- Módulo: objeto que serve como unidade organizacional do código, que é carregado pelo comando de import.
- Pacote: coleção de módulos com hierarquia

# Modularização
    Vantagens da modularização:
        - Legibilidade
        - Manutenção
        - Reaproveitamento do código

# Pacote em Python
Vantagens de criar um pacote:
- Facilidade de compartilhamento
- Facilidade de instalação

# Conceitos
- PyPi: repositório público oficial de pacotes em Python 
- Wheel e Sdist: dois tipos de distribuição para subir o código
- Setuptools: pacotes usados em setup.py para gerar as distribuições (binária) e sdist (source distribution)
- Twine: pacote usado para subir as distribuições do repositório Pypi

# Passos
- 1. Criar um projeto
- 2. Usar o setup.py para distribuir o projeto para gerar as distribuições o wheel e sdist.
- 3. Usar o twine para subir  as distribuições ao Pypi (repositório público)
- 4. Após esses passos, é possivel dar o comando pip install nome_do_pacote para instalar os pacotes

# Tipos de Estruturas
- Simples(apenas 1 módulo)
project_name/
    README.MD
    setup.py
    requirementes.txt
    package_name
        __init__.py
        file1_mane.py
        file2_name.py

Exemplos de chamada para file1_name
--import package_name.file1_name
--from package_name import file1_name

- Com vários módulos
project_name/
    README.MD
    setup.py
    requirementes.txt
    package_name
        __init__.py
        module1_name/
            __init__.py
            file1_mane.py
            file2_name.py
        module2_name/
            __init__.py
            file1_mane.py
            file2_name.py

Exemplos de chamada para file1_name
--import package_name.module1_name.file1_name
--from package_name.module1_name import file1_name

# Repositórios Disponíveis no github
- simple-package-template
- package-template

# Próximos Passos: Criar o Projeto
- Fork do template (recomendado escolher o projeto simples)
- Adição do conteúdo dos módulos do projeto
- Edição do arquivo setup.py (renomear/substituir o nome do(s) pacote(s) e arquivo(s)). É uma boa pratica utilizar aqui o mesmo nome do nome do pacote que será utilizado posteriormente. (para usar o import com o mesmo nome)
- Edição do requirementes.txt (reescrever o texto)
- edição do README.md (reescrever o texto)

# Arquivo setup.py
Usado para especificar como o pacote deve ser construido.
Documentação: hhtps://setuptools.readthedocs.io/en/latest/setuptools.html

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "package_name", # nome coerente 
    version="0.0.1",       # cuidado. manter o formato
    author="my_name",
    author_email="my_email",
    description="My short description",
    long_description=page desctiption,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),  # importante. módulos e submódulos
    install_requires=requirements.txt # só se tiver dependencias de outros pacotes
    pythin_requires='>=3.8', # cuidado para não restringir demais
)

# Arquivo requirementes.txt
Usado para passar os dependências do pacote que devem ser instaldas com o seu pacote. Opcionalmente podem ser especificadas as versões, mas preferencialmente não.

# Arquivo README.MD (usar markdown)
package_name

Description: The package package_name is used for...

Installation
Use the package manager pip to install package_name
pip instal package_name

Usage
from package_name.module1_name import file1_name
file1_name.myfuntion()

Author
My name

License

# Distribuições
Para subir o pacote, criar uma distribuição binária ou distribuição de codigo fonte.
As versões mais recentes do pip instalam primeiramente a bináris e usam a distribuição de código fonte, apenas se necessário.
De qualquer forma, iremos criar ambas a s distribuições.

# Passos para gerar as distrubuições
1. Acessar a raiz do projeto
2. Comandos de instalação
3. Comando para distribuição

# Comandos de instalação (no terminal)
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools

# Comandos para criar distribuição
python setup.py sdist bdist_wheel

# Publicando o Pacote
# Passos para subir o pacote
1. Criar conta no Test Pypi (criar usuário e senhas iguais no Test Pypi e Pypi)
2. Publicar no Test Pypi
3. Instalar pacote usando Test Pypi
4. Testar pacote no local
5. Criar conta no Pypi
6. Publicar no Pypi
7. Instalar pacote usando Pypi

# Criando constas no Pypi
https://test.pypi.org/account/register/
https://pypi.org/account/register/

# Comando (no terminal)para publicar no Test Pypi
python -m twine upload --repository-url
https://test.pypi.org/legacy/ dist/*
após esse comando, será soliliddo username e password
a seguir será feito o upload
verifique se foi atualizado no TestPypi (botao Wiew)

# Comando para instalar o pacote de teste
pip install --index-url https://test.pypi.org/simple/package_name
ou copiar e colar direto o comando no Test Pypi

# Comando para publicar no Pypi (se tudo deu certo...)
python -m twine upload --repository-url
https://upload.pypi.org/legacy/ dist/*
após esse comando, será soliliddo username e password
a seguir será feito o upload
verifique se foi atualizado no Pypi (botão Wiew)

# Comando para instalar o pacote "final"
python -m pip install package_name
ou copiar e colar direto o comando no Test Pypi
talvez seja necessário desinstalar o que foi instalado anteriomente no teste

# Exercício prático
Fazer um pacote usando a estrutura simples de um módulo para testar os conhecimentos adquiridos
simple-package-template

Adicionais:
- Documentação do setuotools:
https://setuptools,readthedocs.io/en/latest/setuptools.html
- Testes automatizados:
https://docs.pytest.org/en/latest/goodpractices.html
- Uso do Tox:
https://tox.readthedocs.io/en/latest/

# Repositórios
simple-package-template
package-template
image-processing-package
https://github.com/tiemi/



