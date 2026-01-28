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
#EXIBIR A LISTA ATUALIZADA NO FINAL


'''
lista_convidados = []

for i in range(10):
    nome = input(f"Digite o nome do convidado {i + 1}: ")
    lista_convidados.append(nome)


adicionar_convidado = input("\nAdicione um novo convidado: ")
if adicionar_convidado in lista_convidados:
    print("Convidado já está na lista.")
else:
    print("Convidado adicionado com sucesso.")
lista_convidados.append(adicionar_convidado)


while True:
    remover_convidado = input(
        f"\nLista atual: {lista_convidados}\n"
        "Digite o nome do convidado a ser removido "
        "(ou pressione ENTER para cancelar): "
    )

    if remover_convidado == "":
        print("Remoção cancelada.")
        break

    elif remover_convidado in lista_convidados:
        lista_convidados.remove(remover_convidado)
        print("Convidado removido com sucesso.")
        break

    else:
        print("Convidado não encontrado. Tente novamente.")


print(f"\nQuantidade atual de convidados: {len(lista_convidados)}")


if lista_convidados:
    print(f"Primeiro convidado: {lista_convidados[0]}")
    print(f"Último convidado: {lista_convidados[-1]}")


if len(lista_convidados) > 1:
    print(f"\nConvidado na posição 1 é: {lista_convidados[1]}")
    novo_nome = input("Digite o novo nome para esse convidado: ")
    lista_convidados[1] = novo_nome
else:
    print("\nNão há convidados suficientes para realizar a alteração.")


print("\nLista de convidados atualizada:")
for convidado in lista_convidados:
    print(convidado)
'''