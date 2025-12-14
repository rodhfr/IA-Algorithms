#Objetivo: juntar tudo: disciplina, sala e restrição de capacidade.

# Disciplinas = [[Matematica, 45 alunos], [historia, 25 alunos]]
# Salas = [[S1, 50 capacidade], [S2, 30 capacidade]]

disciplinas = [{"nome": "Matemática", "alunos": 45}, {"nome": "História", "alunos": 25}]
salas = [{"nome": "S1", "capacidade": 50}, {"nome": "S2", "capacidade": 30}]
salas_alocadas = {sala["nome"]: {"capacidade": sala["capacidade"], "turmas": []} for sala in salas}

"""
Escreva um código que percorra as disciplinas e:
1. Escolha a primeira sala com capacidade suficiente.
2. Imprima qual sala foi alocada para cada disciplina.
"""

for turma in disciplinas:
    for sala_nome, sala_info in salas_alocadas.items():
        if turma["alunos"] <= sala_info["capacidade"]:
            sala_info["capacidade"] -= turma["alunos"]
            sala_info["turmas"].append(turma["nome"])
            print(f'Turma "{turma["nome"]}" com {turma["alunos"]} alunos alocada na sala "{sala_nome}". '
                 f'Capacidade restante: {sala_info["capacidade"]}')
            # sai do loop de salas após alocar
            break  

print("\nSalas alocadas detalhadas:")
for sala_nome, info in salas_alocadas.items():
    print(f'{sala_nome}: {info}')



