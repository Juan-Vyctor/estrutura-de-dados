def verificaEmail(email) :
    posicao = 0;
    posArroba = 0;
    posPonto = 0;

    for caracter in email :
        if caracter == '@' :
            posArroba = posicao;
        elif caracter == '.' :
            posPonto = posicao;
        posicao += 1;
    
    if posArroba > 0 and posPonto > (posArroba + 1) :
        return True;
    else :
        return False;

print("Bem vindo, faça seu cadastro:");
cadastrado = False;

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