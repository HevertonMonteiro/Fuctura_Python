def verificar_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media < 4:
        print('Reprovado!')
    elif media < 7:
        print('Recuperação!')
    else:
        print('Aprovado!')

    return media


quantidade_alunos = int(input('Quantos alunos tem nessa sala? '))
media_geral = 0

for q in range(quantidade_alunos):
    print(f'\nInforme as notas do aluno {q + 1}')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    media = verificar_media(nota1, nota2)
    media_geral += media


media_geral /= quantidade_alunos

print('\n============================')
print(f'A média geral da sala é {media_geral:.2f}')
