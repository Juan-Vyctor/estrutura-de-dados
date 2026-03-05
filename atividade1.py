print("Bem vindo, faça seu cadastro:");

nome = input("Nome: ");
senha = input("Senha: ");
nascimento = input("Data de nascimento: ");
telefone = input("telefone: ");

print(f"""\nCadastro bem sucedido, aqui estão seus dados:
Nome: {nome}
Senha: {senha}
Nascimento: {nascimento}
Telefone: {telefone}""");