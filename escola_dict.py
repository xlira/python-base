##!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.1"

########################################################
#      ATENçÃO: MODIFIQUE ESSE CÓDIGO!                 #
#   Tente utilizar dicionários onde achar conveniente  #
########################################################

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for atividade in atividades:

    print(f"Alunos da atividade {atividade}\n")
    print("-" * 40)

    # sala1 que tem interseção com a atividade

    # print("Sala1 ", atividade_sala1)
    # print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)
