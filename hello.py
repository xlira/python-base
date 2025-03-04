#!/usr/bin/env python ----> Nesse caso você importa as variaveis de ambiente para o interpretador python.

"""Hello World Multi Linguas
Dia 01 - Aula introdutória sobre a linguagem Python e seus conceitos.


Dependendo da lingua configurada no ambiente o programa exibe a correspondente.

Como usar: Tenha a variável LANG devidamente configurada ex:

export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Lucas"
__license__ = "Unlicense"

import os

# caso não tenha uma variavel lang configurada, o padrão vai ser en_US
current_language = os.getenv("LANG", "en_US")[:5]
# fatiar até o quinto caracter para tirar o .utf8, lang[:5]
# split(".")[0] --> antes do ponto
# split(".")[1] --> depois do ponto

# current_language = "en_US"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)  # print é uma função built-in
