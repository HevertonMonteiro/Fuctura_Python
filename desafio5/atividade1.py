nomes = []

menu = int(input(
    "Escolha uma opção do menu (1-4):\n"
    "1. Adicionar nome\n"
    "2. Ver nomes\n"
    "3. Remover nome\n"
    "4. Sair\n"
))

while menu != 4:
    if menu == 1:
        adicionar_nome = input("Digite o nome que deseja adicionar: ")
        nomes.append(adicionar_nome)

    elif menu == 2:
        print("Nomes da lista:")
        for n in nomes:
            print(n)

    elif menu == 3:
        remover_nome = input("Digite o nome que deseja remover: ")
        if remover_nome in nomes:
            nomes.remove(remover_nome)
            print("Nome removido com sucesso.")
        else:
            print("Nome não encontrado.")

    else:
        print("Digite uma opção válida!")

    
    menu = int(input(
        "\nEscolha uma opção do menu (1-4):\n"
        "1. Adicionar nome\n"
        "2. Ver nomes\n"
        "3. Remover nome\n"
        "4. Sair\n"
    ))

print("Programa encerrado.")

