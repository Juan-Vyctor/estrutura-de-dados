from Pessoa import Pessoa;

class No:
    def __init__(self, pessoa=Pessoa):
        self.pessoa = pessoa;
        self.esquerda = None;
        self.direita = None;

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None;
    
    def __inserir(self, no=No, pessoa=Pessoa):
        if no is None:
            return No(pessoa);
    
        # se o atual for menor que o pai, esquerda
        if pessoa.cpf < no.pessoa.cpf:
            no.esquerda = self.__inserir(no.esquerda, pessoa);
        
        # se o atual for maiorque o pai, direita
        elif pessoa.cpf > no.pessoa.cpf:
            no.direita = self.__inserir(no.direita, pessoa);
        
        # senão, ele vira o nó bonitinho
        else:
            no.pessoa = pessoa;
        return no;

    def __buscar(self, no=No, cpf=int):
        if no is None:
            return None;

        # se o CPF tiver no nó, show
        if cpf == no.pessoa.cpf:
            return no.pessoa;

        # se for menor, olha de um lado
        if cpf < no.pessoa.cpf:
            return self.__buscar(no.esquerda, cpf);

        # senão, olha do outro
        return self.__buscar(no.direita, cpf);

    def __menor(self, no=No):
        # auxiliar pra remoção, a ideia é ir descendo no nó até achar o menor descendente o ponto que foi chamado
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def __remover(self, no=No, cpf=int):
        if no is None:
            return None;

        # vai procurando até achar o cpf
        if cpf < no.pessoa.cpf:
            no.esquerda = self.__remover(no.esquerda, cpf);
        elif cpf > no.pessoa.cpf:
            no.direita = self.__remover(no.direita, cpf);
        else:
            # se ele não tem filho nenhum, só zera
            if no.esquerda is None and no.direita is None:
                return None;

            # se ele só tem filho de um lado, só sobe esse filho
            if no.esquerda is None:
                return no.direita;
            if no.direita is None:
                return no.esquerda;

            # se ele tem os dois filhos, tem que achar o menor descendente desse filho >_>
            sucessor = self.__menor(no.direita);

            # achou o descendente, trocou
            no.pessoa = sucessor.pessoa;

            # vai removendo
            no.direita = self.__remover(no.direita, sucessor.pessoa.cpf);

        return no;

    def inserir(self, pessoa=Pessoa):
        self.raiz = self.__inserir(self.raiz, pessoa);
    
    def buscar(self, cpf=int):
        return self.__buscar(self.raiz, cpf);

    def remover(self, cpf=int):

        # esse pedaço aqui do buscar fica a seu critério Thomas, porque é aquele lance "ah checar se tem" e tudo mais mas como é
        # recursivo talvez cague nos gráficos, ai você só tira isso e o "return True" ali embaixo se quiser
        if self.buscar(cpf) is None:
            return False;
    
        self.raiz = self.__remover(self.raiz, cpf);
        return True;

class HashArvore:
    # 10007 foi o número primo mais próximo de 10000, praquele lance de colisão e tudo mais
    def __init__(self, capacidade=100007):
        self.capacidade = capacidade;
        self.tabela = [None] * capacidade;
    
    def hash(self, chave):
        return chave % self.capacidade;

    def adicionar(self, pessoa):
        indice = self.hash(pessoa.cpf);

        # se não tiver ninguém na árvore vai primeiro criar
        if self.tabela[indice] is None:
            self.tabela[indice] = ArvoreBinaria();
        
        self.tabela[indice].inserir(pessoa);
    
    def buscar(self, cpf):
        indice = self.hash(cpf)
        if self.tabela[indice] is None:
            return None;
        return self.tabela[indice].buscar(cpf);

    def remover(self, cpf):

        indice = self.hash(cpf)

        if self.tabela[indice] is None:
            return False

        return self.tabela[indice].remover(cpf)