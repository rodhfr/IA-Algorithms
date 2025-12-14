#Escreva um código que percorra as salas e escolha a primeira que NÃO está ocupada.

salas_disp = [{'nome': 'S1', 'capacidade': 50}, {'nome': 'S2', 'capacidade': 30}]
salas_ocupadas = [{'nome': 'S1', 'capacidade': 50}]

salas = salas_disp + salas_ocupadas
print(salas)

escolha_sala = []

for sala_escolhida in salas:
    if sala_escolhida not in salas_ocupadas:
        print(sala_escolhida)
        escolha_sala.append(sala_escolhida)
        break 
print(f"escolha_sala: {sala_escolhida}")

