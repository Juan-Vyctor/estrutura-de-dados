print("Bem vindo, faça seu cadastro:");
cadastrado = False;

def verificaEmail(email) :
    if '@' in email and '.' in email :
        return True;
    else :
        return False;

while (cadastrado == False):
    nome = input("Nome: ");
    senha = input("Senha: ");
    senha2 = input("Confirme sua senha: ");
    email = input("Email: ");
    telefone = input("telefone: ");

    if (senha != senha2) :
        print("As senhas não coincidem");
    elif (verificaEmail(email) == False):
        print("Email inválido");
    else :
        cadastrado = True;

usuario = {
    'nome': nome,
    'senha': senha,
    'email': email,
    'telefone': telefone,
};

try :
    arquivo = open('./dados/usuarios.bin', "a");
except :
    arquivo = open("./dados/usuarios.bin", "x");

arquivo.write(str(usuario));
arquivo.close();

with open("./dados/usuarios.bin", "r") as arquivo :
    for linha in arquivo :
        print(linha + '\n');