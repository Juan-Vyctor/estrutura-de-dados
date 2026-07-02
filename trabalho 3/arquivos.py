from Pessoa import Pessoa;
import csv;

def carregar_pessoas(arquivo):
    pessoas = [];
    with open(arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile);
        for linha in leitor:
            pessoa = Pessoa(linha["CPF"], linha["Nome"], linha["SobreNome"], linha["Idade"]);
            pessoas.append(pessoa);
    return pessoas

def carregar_cpfs(arquivo):
    cpfs = [];
    with open(arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile);
        next(leitor);
        for linha in leitor:
            cpfs.append(int(linha[0]));
    return cpfs;