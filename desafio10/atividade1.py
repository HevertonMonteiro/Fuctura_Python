def verificar_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media < 4:
        print('Reprovado!')
    elif media >= 7:
        print('Aprovado!')
    else:
        print('Recuperação!')

print('--Insira suas notas--')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

resultado = verificar_media(nota1, nota2, nota3)

print(f'Média final: {resultado:.2f}')




