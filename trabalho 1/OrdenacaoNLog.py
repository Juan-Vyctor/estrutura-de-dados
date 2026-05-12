"""
Arquivo Python para inserção de códigos de algoritmos de ordenação O(n*Log(n))
autor: Arthur Souza
"""

def ordenarIterativoNLog(lista):
    tamanho = len(lista)

    for i in range(tamanho // 2 - 1, -1, -1):
        pai = i

        while True:
            maior = pai
            filhoEsquerda = 2 * pai + 1
            filhoDireita = 2 * pai + 2

            if filhoEsquerda < tamanho and lista[filhoEsquerda] > lista[maior]:
                maior = filhoEsquerda

            if filhoDireita < tamanho and lista[filhoDireita] > lista[maior]:
                maior = filhoDireita

            if maior == pai:
                break

            lista[pai], lista[maior] = lista[maior], lista[pai]
            pai = maior

    for fim in range(tamanho - 1, 0, -1):
        lista[0], lista[fim] = lista[fim], lista[0]
        pai = 0

        while True:
            maior = pai
            filhoEsquerda = 2 * pai + 1
            filhoDireita = 2 * pai + 2

            if filhoEsquerda < fim and lista[filhoEsquerda] > lista[maior]:
                maior = filhoEsquerda

            if filhoDireita < fim and lista[filhoDireita] > lista[maior]:
                maior = filhoDireita

            if maior == pai:
                break

            lista[pai], lista[maior] = lista[maior], lista[pai]
            pai = maior

    return lista

def ordenarRecursivoNLog(lista):
    def heapify(tamanho, entrada):
        maior = entrada
        esquerda = 2 * entrada + 1
        direita = 2 * entrada + 2

        if esquerda < tamanho and lista[esquerda] > lista[maior]:
            maior = esquerda

        if direita < tamanho and lista[direita] > lista[maior]:
            maior = direita

        if maior != entrada:
            lista[entrada], lista[maior] = lista[maior], lista[entrada]
            heapify(tamanho, maior)

    tamanho = len(lista)
    pai = tamanho // 2 - 1

    for i in range(pai, -1, -1):
        heapify(tamanho, i)

    for fim in range(tamanho - 1, 0, -1):
        lista[0], lista[fim] = lista[fim], lista[0]
        heapify(fim, 0)

    return lista