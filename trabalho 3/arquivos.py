from Pessoa import Pessoa
from arvore import HashArvore
from enderecamento import HashTable
import csv


def carregar_pessoas(arquivo):
    pessoas = []
    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            pessoa = Pessoa(linha[0], linha[1], linha[2], linha[3])
            pessoas.append(pessoa)
    return pessoas


def carregar_cpfs(arquivo):
    cpfs = []
    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            cpfs.append(int(linha[0]))
    return cpfs

arvore = HashArvore()
tabela = HashTable()

pessoas = carregar_pessoas('./insercao.csv')
for pessoa in pessoas:
    arvore.adicionar(pessoa)
    tabela.adicionar(pessoa)

cpfs = carregar_cpfs('./busca.csv')
for cpf in cpfs:
    arvore.buscar(cpf)
    tabela.buscar(cpf)

cpfs = carregar_cpfs("./remocao.csv")
for cpf in cpfs:
    arvore.remover(cpf)
    tabela.remover(cpf)
