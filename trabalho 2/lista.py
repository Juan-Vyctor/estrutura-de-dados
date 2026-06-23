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
def listaLigada():
    compras = ListaLigada();
    compras.adicionar("arroz");
    compras.adicionar("feijão");
    compras.adicionar("leite");
    compras.adicionar("pão");
    compras.adicionar("café");

    while True:
        print("\nLISTA DE COMPRAS");
        print("1: Adicionar");
        print("2: Remover");
        print("3: Buscar");
        print("4: Exibir lista");
        print("0: Sair");

        opcao = input("Escolha: ");

        if opcao == "1":
            item = input("Item: ");
            compras.adicionar(item);
            print("Item adicionado");
        elif opcao == "2":
            item = input("Item para remover: ");
            if compras.remover(item):
                print("Item removido");
            else:
                print("Item não encontrado");
        elif opcao == "3":
            item = input("Item para buscar: ");
            if compras.buscar(item):
                print("Item encontrado");
            else:
                print("Item não encontrado");
        elif opcao == "4":
            print("\nLista de compras:");
            compras.exibir();
        elif opcao == "0":
            break;
        else:
            print("Opção inválida");

def listaArray():
    compras = ["arroz", "feijão", "leite", "pão", "café"];

    while True:
        print("\nLISTA DE COMPRAS");
        print("1: Adicionar");
        print("2: Remover");
        print("3: Buscar");
        print("4: Exibir lista");
        print("0: Sair");

        opcao = input("Escolha: ");

        if opcao == "1":
            item = input("Item: ");
            compras.append(item);
            print("Item adicionado");
        elif opcao == "2":
            item = input("Item para remover: ");
            if item in compras:
                compras.remove(item);
                print("Item removido");
            else:
                print("Item não encontrado");
        elif opcao == "3":
            item = input("Item para buscar: ");

            if item in compras:
                print("Item encontrado");
            else:
                print("Item não encontrado");
        elif opcao == "4":
            print("\nLista de compras:");

            if len(compras) == 0:
                print("Lista vazia");
            else:
                for item in compras:
                    print(item);
        elif opcao == "0":
            break;
        else:
            print("Opção inválida");

# listaLigada();
# listaArray();