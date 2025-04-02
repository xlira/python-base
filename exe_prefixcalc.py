##! /usr/bin/python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefixcalc.log`
"""
__version__ = "0.1.0"

import sys

prefix = None
number_1 = None
number_2 = None
operator = None
symbol = None
result = None

operations = ["sum", "sub", "mul", "div"]

args = []
args = sys.argv[1:]
total = len(args)

if total != 0:
    if args[0] in operations:
        operator = args[0]
        number_1 = args[1]
        number_2 = args[2]
    else:
        print(f"Invalid option '{args[0]}'")


while operator == None:
    operator = input("Escolha a operação(sum, sub, mul, div):")
    if operator not in operations:
        print(operator)
        operator = None
        print("Valor invalido, escolha uma das opções citadas.")

if number_1 == None:
    number_1 = int(input("Qual o valor informado para a operação:"))
    int(number_1)

if number_2 == None:
    number_2 = int(input("Qual o outro valor informado para a operação:"))
    int(number_2)

if operator == "sum":
    symbol = "+"
    result = number_1 + number_2
elif operator == "sub":
    symbol = "-"
    result = int(number_1) - int(number_2)
elif operator == "mul":
    symbol = "*"
    result = int(number_1) * int(number_2)
elif operator == "div":
    symbol = "/"
    result = int(number_1) / int(number_2)


print(f"O resultado da operação {number_1} {symbol} {number_2} é: {result}")
