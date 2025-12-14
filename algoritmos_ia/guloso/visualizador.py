# visualizador.py
import time
import os

def mostrar_salas(salas_alocadas, horarios, pausa=2):
    """Mostra o estado atual das salas e horários"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Estado atual das salas:\n")
    header = "Sala   " + "  ".join(horarios)
    print(header)
    print("-" * len(header))
    
    for nome, sala in salas_alocadas.items():
        row = nome.ljust(6)
        for h in horarios:
            row += (sala["horarios"].get(h, "---")).ljust(10)
        print(row)
    
    time.sleep(pausa)

