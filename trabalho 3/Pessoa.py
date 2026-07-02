# pra facilitar e usar nos dois logos
class Pessoa:
    def __init__(self, cpf, nome, sobrenome, idade):
        self.cpf = int(cpf);
        self.nome = nome;
        self.sobrenome = sobrenome;
        self.idade = int(idade);