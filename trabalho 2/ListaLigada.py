class Node:
    def __init__(self, dado):
        self.dado = dado; # dado é o valo
        self.proximo = None; # próximo é o próximo
class ListaLigada:
    def __init__(self):
        self.inicio = None;

    def adicionar(self, item):
        novo = Node(item); # nó apontando pra nada com valor
        if self.inicio is None:
            self.inicio = novo;
            return;
        atual = self.inicio;
        while atual.proximo: # vem andando de um em um até o final
            atual = atual.proximo;
        atual.proximo = novo;

    def remover(self, item):
        atual = self.inicio;
        anterior = None;
        while atual:
            if atual.dado == item: # chegou no certo
                if anterior is None:
                    self.inicio = atual.proximo; # ou coloca no inicio
                else:
                    anterior.proximo = atual.proximo; # ou então "pula" ele
                return True;
            anterior = atual;
            atual = atual.proximo;
        return False;

    def buscar(self, item):
        atual = self.inicio;
        while atual:
            if atual.dado == item:
                return True;
            atual = atual.proximo;
        return False;

    def exibir(self):
        atual = self.inicio;
        if atual is None:
            print("Lista vazia");
            return;
        while atual:
            print(atual.dado);
            atual = atual.proximo;

def testeAdicionar(n):
    lista = ListaLigada();
    for i in range(n): lista.adicionar(i);
def testeRemover(n):
    lista = ListaLigada();
    for i in range(n): lista.adicionar(i);
    for i in range(n): lista.remover(i);
def testeBuscar(n):
    lista = ListaLigada();
    for i in range(n): lista.adicionar(i);
    lista.buscar(n // 2);