#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10
Dia 02 - Aula sobre tipos de dados do Python.
Inteiro, Float, Booleano e NoneType.
"""

__version__ = "0.1.0"
__author__ = "Lucas" 


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros =list(range(1, 11)) # range é um tipo de gerador de numero, é necessario+ 
                         # atribuir o tipo lista para o range

# Iterable (percorriveis)

#para
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("--------------")
