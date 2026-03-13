# import lorem;
# import random;

# 1 - A principal diferença é a possibilidade de alteração das listas. Ambos servem para armazenar
# uma coleção de dados, mas um tuple é constante, e uma vez criado, não pode ser modificado. Uma
# lista, no ententando, pode ser 100% alterada

# 2 - Será exibido os números 40, 30, 20 e 10 numa sequência aleatória, sem repetições. Isso acontece
# porque o método set() ignora entradas duplicadas, assim removendo o 20 e o 40 adicionais

# 3
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
# numeros1 = numeros[0:3];
# numeros2= numeros[5:9];
# print(numeros1, numeros2);

# 4
# letras = {};
# palavra = "banana";
# for letra in palavra:
#     if letra not in letras.keys():
#         quantidade = palavra.count(letra);
#         letras[letra] = quantidade;
#         quantidade = 0;
# print(letras);

# 5
# alunos = {};
# for i in range(3) :
#     alunos[i] = {};
#     alunos[i]["nome"] = lorem.sentence();
#     alunos[i]["notas"] = {
#         "nota 1" : random.randint(1, 10),
#         "nota 2" : random.randint(1, 10),
#         "nota 3" : random.randint(1, 10),
#     };
# print(alunos);

# 6
# dicioNomes = {};
# nomes = ["ana", "bia", "caio"];
# for nome in nomes :
#     dicioNomes[nome] = len(nome);
# print(dicioNomes);

# 7
# jogadores = [
#     {"nome": "A", "pontos": 10},
#     {"nome": "B", "pontos": 50},
#     {"nome": "C", "pontos": 30},
# ];
# for i in range(0, len(jogadores)-1):
#     if jogadores[i]["pontos"] < jogadores[i+1]["pontos"]:
#         jogadores.insert(i, jogadores.pop(i+1));
# print(jogadores);

# 8
# carrinho = [];
# carrinho.append("Celular");
# carrinho.append("Fone");
# carrinho.append("Capa")
# carrinho.pop(2);
# print(carrinho);

# 9
# frutas = {
#     "maçã": 10,
#     "banana": 15
# };
# frutas["banana"] = 20;
# frutas["uva"] = 5;
# for fruta in frutas.keys() :
#     if frutas[fruta] > 0:
#         print(fruta);