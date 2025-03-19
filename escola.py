#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala
# CONTINUE O CÓDIGO AQUI

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica), 
    ("Dança", aula_danca)
    ]
atividade_sala1 = []
atividade_sala2 = []

for atividade, nome in atividades:
    print(f"Aula de {atividade}")
    print("-" * 40)

    for aluno in nome:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(atividade_sala1)
    print(atividade_sala2)
    print("#" * 40)
