#Objetivo: juntar tudo: disciplina, sala e restrição de capacidade.


disciplinas = [
        {"nome": "Calculo-I", "alunos": 60, "preferencia": "manha"}, 
        {"nome": "IntroIA", "alunos": 25, "preferencia": "tarde"},
        {"nome": "Calculo-III", "alunos": 50, "preferencia": "tarde"}, 
        {"nome": "Calculo-III", "alunos": 60, "preferencia": "tarde"}, 
        {"nome": "Algebra-Linear", "alunos": 15, "preferencia": "manha"},
        {"nome": "Estatistica", "alunos": 20, "preferencia": "manha"}
]

salas = [
        {"nome": "S1", "capacidade": 50}, 
        {"nome": "S2", "capacidade": 30},
        {"nome": "S3", "capacidade": 20},
        {"nome": "S4", "capacidade": 60},
        {"nome": "S5", "capacidade": 15},
        {"nome": "S6", "capacidade": 60}, 
]


salas_alocadas = {
        sala["nome"]: {
                     "capacidade": sala["capacidade"], 
                     "horarios": {},
                     "turmas": []
                     } 
        for sala in salas 
}

horarios = ["manha", "tarde"]


"""
Escreva um código que:
1. Tente colocar a disciplina na sala disponível no horário preferido.
2. Se não houver sala livre nesse horário, tente outro horário.
3. Imprima a sala e horário escolhidos.
"""

disciplinas_ordenadas = sorted(disciplinas, key=lambda t: t["alunos"], reverse=True)

turmas_nao_alocadas = disciplinas_ordenadas.copy()

for turma in turmas_nao_alocadas:
    alocada = False
    for h in [turma["preferencia"]] + [x for x in horarios if x != turma["preferencia"]]:
        # salas que cabem na turma e estão livres no horário
        salas_disponiveis = [(nome, s) for nome, s in salas_alocadas.items() if h not in s["horarios"] and s["capacidade"] >= turma["alunos"]]
        if salas_disponiveis:
            # escolha da sala: a que mais se aproxima do tamanho da turma
            sala_nome, sala = min(salas_disponiveis, key=lambda x: x[1]["capacidade"] - turma["alunos"])
            sala["horarios"][h] = turma["nome"]
            sala["capacidade"] -= turma["alunos"]
            sala["turmas"].append(turma["nome"])
            alocada = True
            print(f'Turma "{turma["nome"]}" alocada na sala "{sala_nome}" no horário "{h}". Capacidade restante: {sala["capacidade"]}')
            break
    if not alocada:
        print(f'Turma "{turma["nome"]}" não pôde ser alocada em nenhum horário.')

print("\nSalas alocadas detalhadas:")
for sala_nome, sala in salas_alocadas.items():
    print(f'{sala_nome}: Capacidade restante {sala["capacidade"]}, Horários: {sala["horarios"]}, Turmas: {sala["turmas"]}')


