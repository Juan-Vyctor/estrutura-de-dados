from Pessoa import Pessoa;

class HashTable:
    # isso tá aqui porque como o alocamento é linear, se a gente só excluir fisicamente dá pau nas buscas e tudo mais
    removido = object();

    # 10007 foi o número primo mais próximo de 10000, praquele lance de colisão e tudo mais
    def __init__(self, capacidade=10007):
        self.capacidade = capacidade;
        self.tabela = [None] * capacidade;
    
    def hash(self, chave):
        return chave % self.capacidade;

    def adicionar(self, pessoa=Pessoa):
        indice = self.hash(pessoa.cpf);

        # enquanto tiver tendo gente
        while self.tabela[indice] is not None and self.tabela[indice] != self.removido:

            # vê se a chave bate com a que a gente quer pra fazer a mudança
            if self.tabela[indice].cpf == pessoa.cpf:
                self.tabela[indice] = pessoa;
                return;
        
            indice = (indice + 1) % self.capacidade;
        self.tabela[indice] = pessoa;
    
    def buscar(self, cpf):
        indice = self.hash(cpf);
        inicio = indice;

        # enquanto tiver gente
        while self.tabela[indice] is not None:
            if self.tabela[indice] != self.removido:

                # vai procurando a pessoa pela chave e andando
                if self.tabela[indice].cpf == cpf:
                    return self.tabela[indice];
            indice = (indice + 1) % self.capacidade;

            #  se nem chegou a andar, tchau
            if indice == inicio:
                break;
        return None;
    
    def remover(self, cpf):
        indice = self.hash(cpf);
        inicio = indice;

        # enquanto tiver coisa
        while self.tabela[indice] is not None:

            # se não for removido >E< o CPF for o que a gente quer, remove
            if self.tabela[indice] != self.removido and self.tabela[indice].cpf == cpf:
                self.tabela[indice] = self.removido;
                return True;
            indice = (indice + 1) % self.capacidade;

            # se nem chegou a andar, tchau
            if indice == inicio:
                break;
        return False;