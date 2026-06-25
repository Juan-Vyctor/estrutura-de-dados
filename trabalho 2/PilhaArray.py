class Pilha:
    def __init__(self):
        self.capacidade = 1;
        self.itens = 0;
        self.array = [None] * self.capacidade;
    def aumentaTamanho(self):
        capacidade = self.capacidade * 2;
        array = [None] * capacidade;
        for i in range(self.itens): array[i] = self.array[i];
        self.array = array;
        self.capacidade = capacidade;
    def diminuiTamanho(self):
        capacidade = self.capacidade // 2;
        if capacidade == 0 : capacidade = 1;
        array = [None] * capacidade;
        for i in range(self.itens): array[i] = self.array[i];
        self.array = array;
        self.capacidade = capacidade;
    def push(self, item):
        if self.itens == self.capacidade: self.aumentaTamanho();
        self.array[self.itens] = item;
        self.itens += 1;
    def pop(self):
        if self.itens == 0: return;
        self.itens -= 1;
        item = self.array[self.itens];
        self.array[self.itens] = None;
        if self.itens > 0 and self.itens <= self.capacidade // 2: self.diminuiTamanho();
        return item;
    def topo(self):
        if self.itens == 0: return None;
        return self.array[-1];
    def exibir(self):
        for i in range(self.itens-1, -1, -1): print(self.array[i]);

def testeAdicionar(n):
    pilha = Pilha();
    for i in range(n): pilha.push(i);
def testeRemover(n):
    pilha = Pilha();
    for i in range(n): pilha.push(i);
    for i in range(n): pilha.pop();
def testeTop(n):
    pilha = Pilha();
    for i in range(n): pilha.append(i);
    pilha.topo();