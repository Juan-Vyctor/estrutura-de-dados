"""
Arquivo Python para inserção de códigos de algoritmos de ordenação O(n^2)
autor: Arthur Souza
"""

def ordenarIterativoN2(lista):
    n = len(lista)
    intervalo = n
    reducao = 1.3
    ordenado = False

    while not ordenado:
        intervalo = int(intervalo / reducao)
        if intervalo <= 1:
            intervalo = 1
            ordenado = True

        for i in range(0, n - intervalo):
            if lista[i] > lista[i + intervalo]:
                lista[i], lista[i + intervalo] = lista[i + intervalo], lista[i]
                ordenado = False


def ordenarRecursivoN2(lista, intervalo = None):
    if intervalo is None:
        intervalo = len(lista)
    reducao = 1.3
    ordenado = False

    intervalo = int(intervalo / reducao)

    if intervalo <= 1:
        intervalo = 1
        ordenado = True

    for i in range(0, len(lista) - intervalo):
        if lista[i] > lista[i + intervalo]:
            lista[i], lista[i + intervalo] = (lista[i + intervalo], lista[i])

    if intervalo != 1 or not ordenado:
        return ordenarRecursivoN2(lista, intervalo)

    return lista