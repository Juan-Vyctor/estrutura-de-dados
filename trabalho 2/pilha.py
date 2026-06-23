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
def pilhaLigada():
    historico = PilhaLigada();
    historico.push("google.com");
    historico.push("youtube.com");
    historico.push("wikipedia.org");

    while True:
        print("\nHISTÓRICO DE NAVEGAÇÃO");
        print("1: Visitar página");
        print("2: Voltar página");
        print("3: Página atual");
        print("4: Exibir histórico");
        print("0: Sair");

        opcao = input("Escolha: ");

        if opcao == "1":
            pagina = input("Página: ");
            historico.push(pagina);
            print("Página adicionada");

        elif opcao == "2":
            removida = historico.pop();
            if removida is not None:
                print("Voltou da página: ", removida);
            else:
                print("Histórico vazio");
        elif opcao == "3":
            atual = historico.peek();
            if atual is not None:
                print("Página atual: ", atual);
            else:
                print("Nenhuma página aberta");
        elif opcao == "4":
            print("\nHistórico:");
            historico.exibir();
        elif opcao == "0":
            break;
        else:
            print("Opção inválida");

def pilhaArray():
    historico = ["google.com", "youtube.com", "wikipedia.org"];

    while True:
        print("\nHISTÓRICO DE NAVEGAÇÃO");
        print("1: Visitar página");
        print("2: Voltar página");
        print("3: Página atual");
        print("4: Exibir histórico");
        print("0: Sair");

        opcao = input("Escolha: ");

        if opcao == "1":
            pagina = input("Página: ");
            historico.append(pagina);
            print("Página adicionada");
        elif opcao == "2":
            if len(historico) > 0:
                removida = historico.pop();
                print("Voltou da página: ", removida);
            else:
                print("Histórico vazio");
        elif opcao == "3":
            if len(historico) > 0:
                print("Página atual: ", historico[-1]);
            else:
                print("Nenhuma página aberta");
        elif opcao == "4":
            if len(historico) == 0:
                print("Histórico vazio");
            else:
                print("\nHistórico:");
                for pagina in reversed(historico):
                    print(pagina);
        elif opcao == "0":
            break;
        else:
            print("Opção inválida");

# pilhaLigada();
# pilhaArray();