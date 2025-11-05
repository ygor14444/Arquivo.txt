def cadastrar_usuario():
    nome = input("digite o seu nome:")
    idade = input("digite a sua idade:")
    email = input("digite o seu email:")
    with open("usuarios.txt","a") as arquivo:
        arquivo.write(f"nome: {nome}, idade: {idade}, email: {email}\n")
    print("usuario cadastrado com sucesso!!\n")
def listar_usuarios():
    try:
        with open ("usuarios.txt","r") as arquivo:
            conteudo = arquivo.read()
        if conteudo =="":
            print("nenhum usuario cadastrado")
        else:
            print("\n lista de usuarios cadastrados:")
            print(conteudo)
    except FileNotFoundError:
        print("nenhum usuario cadastrado ainda")

while True:
    print("__________MENU__________")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Sair")

    opcao = input("Digite uma opçao:")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        print("encerrando o programa...")
        break
    else:
        print("Opçao invalida. Tente novamente!")