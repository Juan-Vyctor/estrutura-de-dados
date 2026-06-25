class Node:
    def __init__(self, dado):
        self.dado = dado;
        self.proximo = None;
class FilaLigada:
    def __init__(self):
        self.inicio = None;
        self.fim = None;
    def enfileirar(self, item):
        novo = Node(item);
        if self.fim is None:
            self.inicio = novo;
            self.fim = novo;
            return;
        self.fim.proximo = novo;
        self.fim = novo;
    def remover(self):
        if self.inicio is None:
            return None;
        removido = self.inicio.dado;
        self.inicio = self.inicio.proximo;
        if self.inicio is None:
            self.fim = None;
        return removido;
    def front(self):
        if self.inicio is None:
            return None;
        return self.inicio.dado;
    def exibir(self):
        if self.inicio is None:
            print("Fila vazia");
            return;
        atual = self.inicio;
        while atual:
            print(atual.dado);
            atual = atual.proximo;

def testeAdicionar(n):
    fila = FilaLigada();
    for i in range(n): fila.enfileirar(i);
def testeRemover(n):
    fila = FilaLigada();
    for i in range(n): fila.enfileirar(i);
    for i in range(n): fila.remover();
def testeFront(n):
    fila = FilaLigada();
    for i in range(n): fila.enfileirar(i);
    fila.front();