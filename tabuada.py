##!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10
Dia 02 - Aula sobre tipos de dados do Python.
Inteiro, Float, Booleano e NoneType.

Especificação

---Tabuada do 1---
    1 x 1 = 1
...
##################
"""
__version__ = "0.1.1"
__author__ = "Lucas"

template = """
---Tabuada do 2---

    {bloco}

##################
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))  # range é um tipo de gerador de numero, é necessario+
# atribuir o tipo lista para o range

# Iterable (percorriveis)

# para
for n1 in numeros:
    print(
        "{:-^18}".format(f"Tabuada do {n1}")
    )  # imprime o titulo centralizado em 18 espaços, com - antes e depois, pega o numero atual do for.
    print()  # pula linha
    for n2 in numeros:
        resultado = (
            n1 * n2
        )  # pega o numero do primeiro for e multiplica pelo numero do segundo for
        print(
            "{:^18}".format(f"{n1} x {n2} = {resultado}")
        )  # imprime a linha da multiplicacao da tabuada, fazendo o primeiro for vezes o segundo for, centraliza eles em 18 espaços.
    print("#" * 18)  # separa uma tabuada da outra com 18 hashtags.
