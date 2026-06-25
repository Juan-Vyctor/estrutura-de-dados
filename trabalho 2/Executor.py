import time;
import random;
import os;

def medirTempo(funcao, entrada):
    inicio = time.perf_counter();
    funcao(entrada);
    fim = time.perf_counter();
    return (fim - inicio)*1000;

import ListaArray as la;
import ListaLigada as ll;
import FilaArray as fa;
import FilaLigada as fl;
import PilhaArray as pa;
import PilhaLigada as pl;
    
def salvaResultado(algoritmo, n, resultado):
    os.makedirs("resultados", exist_ok=True);
    caminhoArquivo = os.path.join("resultados", f"{algoritmo}.res");
    with open(caminhoArquivo, "w") as arquivo:
        arquivo.write(f"{algoritmo};{n}\n");
        for item in resultado: arquivo.write(str(item) + "\n");

def executaExperimento(nome, funcao, n):
    resultado = [];
    for i in range(1, n + 1):
        if i % (n // 10) == 0: print(f"Executando {nome}: {i}");
        resultado.append(medirTempo(funcao, i));
    salvaResultado(nome, n, resultado);
    print(f"Finalizado experimento para {nome}");

   
if __name__ == "__main__":
    opcoes = [
        "ListaArray-Adicionar",
        "ListaArray-Remover",
        "ListaLigada-Adicionar",
        "ListaLigada-Remover",
        "FilaArray-Adicionar",
        "FilaArray-Remover",
        "FilaLigada-Adicionar",
        "FilaLigada-Remover",
        "PilhaArray-Adicionar",
        "PilhaArray-Remover",
        "PilhaLigada-Adicionar",
        "PilhaLigada-Remover"
    ];
    funcoes = [
        la.testeAdicionar,
        la.testeRemover,
        ll.testeAdicionar,
        ll.testeRemover,
        fa.testeAdicionar,
        fa.testeRemover,
        fl.testeAdicionar,
        fl.testeRemover,
        pa.testeAdicionar,
        pa.testeRemover,
        pl.testeAdicionar,
        pl.testeRemover
    ];

    for i in range(len(opcoes)):
        print(f"[{i+1}] {opcoes[i]}");

    opcao = int(input("Escolha o experimento: "));
    if opcao > 0 and opcao <= len(funcoes):
        n = int(input("Informe o valor máximo de n: "));
        print("Executando experimento...");
        executaExperimento(opcoes[opcao - 1], funcoes[opcao - 1], n);