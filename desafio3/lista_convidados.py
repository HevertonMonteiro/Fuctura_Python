#EXERCICIO SOLICITADO
lista_convidados = [
    "Ana Silva",
    "Bruno Souza",
    "Carla Mendes",
    "Daniel Oliveira",
    "Eduarda Lima",
    "Felipe Costa",
    "Gabriela Rocha",
    "Hugo Fernandes",
    "Isabela Martins",
    "João Pereira"
]

adicionar_convidado = ("Thomas Almeida",)
lista_convidados.append(adicionar_convidado[-1])

remover_convidado = "Daniel Oliveira"
lista_convidados.remove(remover_convidado)
print(f"Primeiro convidado: {lista_convidados[0]}", "Ultimo convidado:", f"{lista_convidados[-1]}", sep="\n")

alterar_convidado = "Bruno Souza"
lista_convidados[1] = "Pedro Silva"

print("Lista de convidados atualizada:")
for convidado in lista_convidados:
    print(convidado)




#EXERCICIO EXTRA ULTILIZANDO FOR/WHILE/IF 
#SOLICITAR INCLUSAO DA LISTA VIA INPUT
#REALIZAR A INCLUSÃO, REMOÇÃO E ALTERAÇÃO DE NOMES VIA INPUT
#UTILIZAR REPETIÇÃO PARA TER CERTEZA QUE A ALTERAÇÃO FOI REALIZADA OU NÃO
#FALTOU ADICIONAR O LOOPING E VERIFICAÇÃO PARA REMOÇÃO TAMBÉM
#EXIBIR A LISTA ATUALIZADA NO FINAL

'''
lista_convidados = []

for i in range(10):
    nome = input(f"Digite o nome do convidado {i + 1}: ")
    lista_convidados.append(nome)

adicionar_convidado = input("Adicione um conviadado: ")
lista_convidados.append(adicionar_convidado)

remover_convidado = input("Digite o nome do convidado a ser removido: ")
if remover_convidado in lista_convidados:
    lista_convidados.remove(remover_convidado)
    print(f"Primeiro convidado: {lista_convidados[0]}", "Ultimo convidado:" f"{lista_convidados[-1]}", sep="\n")
else:
    print("Convidado não encontrado na lista.")

while True:
    alterar_convidado = input(
        f"\nLista atual: {lista_convidados}\n"
        "Digite o nome do convidado que deseja alterar "
        "(ou pressione ENTER para não alterar mais): "
    )
    if alterar_convidado == "":
        print("Nenhuma alteração adicional realizada.")
        break

    elif alterar_convidado in lista_convidados:
        indice = lista_convidados.index(alterar_convidado)
        novo_convidado = input("Digite o novo nome do convidado: ")

        if novo_convidado:
            lista_convidados[indice] = novo_convidado
            print("Convidado alterado com sucesso.")
        else:
            print("Nome inválido. Alteração cancelada.")

        continuar = input("Deseja alterar outro convidado? (s/n): ").lower()
        if continuar != "s":
            break

    else:
        print("Convidado não encontrado. Tente novamente.")



print("Lista de convidados atualizada:")
for convidado in lista_convidados:
    print(convidado)
'''