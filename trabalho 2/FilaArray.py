class Fila:
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
    def pop(self):
        if self.itens == 0: return;
        item = self.array[0];
        self.array[0] = None;
        for i in range(1, self.itens): self.array[i-1] = self.array[i];
        self.itens -= 1;
        if self.itens > 0 and self.itens <= self.capacidade // 2: self.diminuiTamanho();
        return item;
    def front(self):
        if self.itens == 0: return None;
        return self.array[0];
    def exibir(self):
        for i in range(self.itens): print(self.array[i]);

def testeAdicionar(n):
    fila = Fila();
    for i in range(n): fila.append(i);
def testeRemover(n):
    fila = Fila();
    for i in range(n): fila.append(i);
    fila.pop();
def testeFront(n):
    fila = Fila();
    for i in range(n): fila.append(i);
    fila.front();