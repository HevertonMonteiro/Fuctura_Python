def verificar_media(nota1, nota2):
    return(nota1+nota2)/2

quantidade_alunos = int(input('Quantos alunos tem nessa sala? '))
media_geral = 0
for q in range (quantidade_alunos):

    print(f'\nInforme suas notas: {q+1} ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 1: '))

    media = verificar_media(nota1, nota2)
    media_geral += media / quantidade_alunos

    if media < 4:
        print('Reprovado! ')
    elif media == 7:
        print('Aprovado por Media! ')
    elif media > 7:
        print('Aprovado! ')
    else:
        print('Recuperação! ')

print('\n============================')
print(f'A media geral da sala é {media_geral: .2f}')
