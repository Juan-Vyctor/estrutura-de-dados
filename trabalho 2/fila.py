class Node:
    def __init__(self, dado):
        self.dado = dado;
        self.proximo = None;
class FilaLigada:
    def __init__(self):
        self.inicio = None;
        self.fim = None;

    def enfilar(self, item):
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
def filaLigada():
    fila = FilaLigada();
    fila.enfilar("Ana");
    fila.enfilar("Bruno");
    fila.enfilar("Carlos");
    fila.enfilar("Daniela");
    fila.enfilar("Eduardo");

    while True:
        print("\nFILA DE ATENDIMENTO");
        print("1: Entrar na fila");
        print("2: Atender próximo");
        print("3: Próximo da fila");
        print("4: Exibir fila");
        print("0: Sair");

        opcao = input("Escolha: ");

        if opcao == "1":
            pessoa = input("Nome: ");
            fila.enfilar(pessoa);
            print("Pessoa adicionada à fila");
        elif opcao == "2":
            atendido = fila.remover();
            if atendido is not None:
                print("Atendido:", atendido);
            else:
                print("Fila vazia");
        elif opcao == "3":
            proximo = fila.front();
            if proximo is not None:
                print("Próximo:", proximo);
            else:
                print("Fila vazia");
        elif opcao == "4":
            print("\nFila atual:");
            fila.exibir();
        elif opcao == "0":
            break;
        else:
            print("Opção inválida");

def filaArray():
    fila = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"];

    while True:
        print("\nFILA DE ATENDIMENTO");
        print("1: Entrar na fila");
        print("2: Atender próximo");
        print("3: Próximo da fila");
        print("4: Exibir fila");
        print("0: Sair");

        opcao = input("Escolha: ");

        if opcao == "1":
            pessoa = input("Nome: ");
            fila.append(pessoa);
            print("Pessoa adicionada à fila");
        elif opcao == "2":
            if len(fila) > 0:
                atendido = fila.pop(0);
                print("Atendido: ", atendido);
            else:
                print("Fila vazia");
        elif opcao == "3":
            if len(fila) > 0:
                print("Próximo: ", fila[0]);
            else:
                print("Fila vazia");
        elif opcao == "4":
            if len(fila) == 0:
                print("Fila vazia");
            else:
                print("\nFila atual:");
                for pessoa in fila:
                    print(pessoa);
        elif opcao == "0":
            break;
        else:
            print("Opção inválida");

# filaLigada();
# filaArray();