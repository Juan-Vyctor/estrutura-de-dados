# Considere uma função que recebe duas listas e returne quantas instâncias de cada elemento da lista 2 existem na lista 1

def contaItensFor(lista, busca) :
    totais = {};

    for itemProcurado in busca :
        instancias = 0;
        for itemRetornado in lista :
            if itemProcurado == itemRetornado :
                instancias += 1;
        totais[itemProcurado] = instancias;

    return totais;
def contaItensCount(lista, busca) :
    totais = {};

    for itemProcurado in busca:
        totais[itemProcurado] = lista.count(itemProcurado);

    return totais;
# print("Usando for:", contaItensFor(
#         [1, 1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 7, 9, 9, 9],
#         [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     )
# );
# print("Usando count:", contaItensCount(
#         [1, 1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 7, 9, 9, 9],
#         [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     )
# );

def retornaRepetidos(lista) :
    vistos = [];
    repetidos = [];
    for item in lista :
        if item not in vistos :
            vistos.append(item);
        elif item not in repetidos :
            repetidos.append(item);

    return repetidos;
print(retornaRepetidos([1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8, 9, 9 ]));