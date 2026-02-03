nomes = []

menu = 0

while menu != 4:

    try:
        menu = int(input(
        "\nEscolha uma opção do menu (1-4):\n"
        "1. Adicionar nome\n"
        "2. Ver nomes\n"
        "3. Remover nome\n"
        "4. Sair\n"
    ))
    except ValueError:
        print("Digite apenas numeros! ")
        continue

    if menu == 1:
        adicionar_nome = input("Digite o nome que deseja adicionar: ")
        nomes.append(adicionar_nome)

    elif menu == 2:
        if len(nomes) == 0:
            print("lista vazia ")
        else:
            print("Nomes na lista: ")
        for n in nomes:
            print(n)

    elif menu == 3:
        remover_nome = input("Digite o nome que deseja remover: ")
        if remover_nome in nomes:
            nomes.remove(remover_nome)
            print("Nome removido com sucesso.")
        else:
            print("Nome não encontrado.")

    elif menu == 4:
        print("Programa encerrado.")

    



