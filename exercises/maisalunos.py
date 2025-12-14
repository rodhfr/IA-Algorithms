from operator import itemgetter

disciplinas = [
    {"nome": "Matemática", "alunos": 45},
    {"nome": "História", "alunos": 25},
    {"nome": "Biologia", "alunos": 35}
]

# itemgetter pega uma funcao que dado um dicionario retorna dicionario["key"]. Equivalente a lambda x: x["alunos"].
# https://www.geeksforgeeks.org/python/itemgetter-in-python/
disciplina_por_tamanho = sorted(disciplinas, key=itemgetter("alunos"), reverse=True)
print(disciplina_por_tamanho)

