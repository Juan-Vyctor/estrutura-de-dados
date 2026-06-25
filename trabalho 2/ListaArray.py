class Lista:
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
    def append(self, item):
        if self.itens == self.capacidade: self.aumentaTamanho();
        self.array[self.itens] = item;
        self.itens += 1;
    def remove(self, posicao):
        if posicao < 0 or posicao >= self.itens: return;
        item = self.array[posicao];
        for i in range(posicao + 1, self.itens): self.array[i - 1] = self.array[i];
        self.itens -= 1;
        self.array[self.itens] = None;
        if self.itens > 0 and self.itens <= self.capacidade // 2: self.diminuiTamanho();
        return item;
    def exibir(self):
        for i in range(self.itens): print(self.array[i]);
    def peek(self, posicao):
        return self.array[posicao];

def testeAdicionar(n):
    lista = Lista();
    for i in range(n): lista.append(i);
def testeRemover(n):
    lista = Lista();
    for i in range(n): lista.append(i);
    for i in range(n): lista.remove(0);
def testePeek(n):
    lista = Lista();
    for i in range(n): lista.append(i);
    lista.peek(n // 2);