class Node:
    def __init__(self, dado):
        self.dado = dado;
        self.proximo = None;
class PilhaLigada:
    def __init__(self):
        self.topo = None;
    def push(self, item):
        novo = Node(item);
        novo.proximo = self.topo;
        self.topo = novo;
    def pop(self):
        if self.topo is None:
            return None;
        removido = self.topo.dado;
        self.topo = self.topo.proximo;
        return removido;
    def peek(self):
        if self.topo is None:
            return None;
        return self.topo.dado;
    def exibir(self):
        if self.topo is None:
            print("Histórico vazio");
            return;
        atual = self.topo;
        while atual:
            print(atual.dado);
            atual = atual.proximo;

def testeAdicionar(n):
    pilha = PilhaLigada();
    for i in range(n): pilha.push(i);
def testeRemover(n):
    pilha = PilhaLigada();
    for i in range(n): pilha.push(i);
    for i in range(n): pilha.pop();
def testePeek(n):
    pilha = PilhaLigada();
    for i in range(n): pilha.push(i);
    pilha.peek();