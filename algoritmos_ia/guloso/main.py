from visualizador import mostrar_salas
import time

# ---------------- Dados iniciais ----------------
professores = [
    {"nome": "Bidu", "preferencia": "LPII"},
    {"nome": "Teobaldo", "preferencia": "PO"},
    {"nome": "Lucidio", "preferencia": "IntroIA"},
    {"nome": "Gilberto", "preferencia": "EstruturaDados"},
    {"nome": "Yuri", "preferencia": "introCDIA"},
]

professores_alocados = {
    professor["nome"]: {"sala": [], "horarios": {}} for professor in professores
}

disciplinas = [
    {"nome": "LPII", "alunos": 60, "preferencia": "manha"},
    {"nome": "IntroCDIA", "alunos": 25, "preferencia": "tarde"},
    {"nome": "EstruturaDados", "alunos": 50, "preferencia": "tarde"},
    {"nome": "APA", "alunos": 60, "preferencia": "tarde"},
    {"nome": "IntroIA", "alunos": 15, "preferencia": "manha"},
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
    sala["nome"]: {"capacidade": sala["capacidade"], "horarios": {}, "turmas": [], "professores": []} 
    for sala in salas
}

horarios = ["manha", "tarde"]

""" 
RESTRICOES:
Turma: 
    - Cada disciplina deve estar alocada em exatamente uma sala e em exatamente um horário. 
    - Deve ter um professor atribuído. 
Salas: 
    - A sala escolhida deve ter capacidade suficiente para o número de alunos da turma. 
    - Preferir a sala cuja capacidade seja mais próxima do tamanho da turma, evitando desperdício. 
    - Uma sala não pode ter mais de uma disciplina no mesmo horário.
    - Cada sala mantém registro dos horários ocupados, turmas e professores alocados. 
Professor: 
    - Um professor só pode dar uma disciplina por horário. 
    - Priorizar professores que têm preferência pela disciplina. 
    - Caso não haja professor com preferência disponível, escolher o professor disponível com menos turmas alocadas até o momento. 
    - Cada professor mantém registro dos horários e das salas em que está alocado.
    - Se nenhum professor estiver disponível em todos os horários, a turma fica como não alocada. 
Horários: 
    - Tentar primeiro o horário preferido da disciplina; se não for possível, tentar outros horários disponíveis. 
    - Cada turma só pode ser alocada em um horário. 
    - Cada sala e professor só podem ter uma disciplina por horário. 
"""
# ---------------- Configuração da velocidade ----------------
velocidade = 0.5  # segundos de pausa entre prints e visualizador

# Ordena disciplinas por número de alunos (do maior para o menor)
disciplinas_ordenadas = sorted(disciplinas, key=lambda t: t["alunos"], reverse=True)
turmas_nao_alocadas = disciplinas_ordenadas.copy()

# ---------------- Alocação gulosa ----------------
for turma in turmas_nao_alocadas:
    alocada = False
    print(f'\nTentando alocar turma "{turma["nome"]}" com {turma["alunos"]} alunos.')
    time.sleep(velocidade)
    
    for h in [turma["preferencia"]] + [x for x in horarios if x != turma["preferencia"]]:
        print(f'  Tentando horário: "{h}"')
        time.sleep(velocidade)

        salas_disponiveis = [(nome, s) for nome, s in salas_alocadas.items() if h not in s["horarios"] and s["capacidade"] >= turma["alunos"]]
        print(f'    Salas disponíveis: {[s[0] for s in salas_disponiveis]}')
        time.sleep(velocidade)

        if not salas_disponiveis:
            continue

        sala_nome, sala = min(salas_disponiveis, key=lambda x: x[1]["capacidade"] - turma["alunos"])
        print(f'    Sala escolhida: "{sala_nome}"')
        time.sleep(velocidade)

        professores_disponiveis = [p for p in professores if h not in professores_alocados[p["nome"]]["horarios"]]
        professores_pref_disc = [p for p in professores_disponiveis if p["preferencia"] == turma["nome"]]

        if professores_pref_disc:
            professor = min(professores_pref_disc, key=lambda p: len(professores_alocados[p["nome"]]["horarios"]))
            print(f'    Professor preferencial disponível: "{professor["nome"]}"')
        else:
            professor = min(professores_disponiveis, key=lambda p: len(professores_alocados[p["nome"]]["horarios"]))
            print(f'    Nenhum preferencial disponível, professor escolhido com menos turmas: "{professor["nome"]}"')
        time.sleep(velocidade)

        # Atualiza a alocação
        sala["horarios"][h] = turma["nome"]
        sala["capacidade"] -= turma["alunos"]
        sala["turmas"].append(turma["nome"])
        professores_alocados[professor["nome"]]["horarios"][h] = turma["nome"]
        professores_alocados[professor["nome"]]["sala"].append(sala_nome)

        alocada = True
        print(f'    Turma "{turma["nome"]}" alocada na sala "{sala_nome}" no horário "{h}" com professor "{professor["nome"]}". capacidade restante: {sala["capacidade"]}')
        time.sleep(velocidade)

        # Atualiza visualização
        mostrar_salas(salas_alocadas, horarios, pausa=velocidade)
        break

    if not alocada:
        print(f'    Turma "{turma["nome"]}" não pôde ser alocada em nenhum horário.')
        time.sleep(velocidade)
        mostrar_salas(salas_alocadas, horarios, pausa=velocidade)

# ---------------- Resultados finais ----------------
print("\nSalas alocadas detalhadas:")
for sala_nome, sala in salas_alocadas.items():
    print(f'{sala_nome}: capacidade restante {sala["capacidade"]}, horários: {sala["horarios"]}, turmas: {sala["turmas"]}')

print("\nProfessores alocados detalhados:")
for prof_nome, info in professores_alocados.items():
    print(f'{prof_nome}: salas {info["sala"]}, horários: {info["horarios"]}, total de turmas: {len(info["horarios"])}')

