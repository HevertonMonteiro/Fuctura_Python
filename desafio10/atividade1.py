def verificar_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
print('--Insira suas notas--')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

media = verificar_media(nota1, nota2, nota3)

if media < 4:
    print('Reprovado!')
elif media >= 7:
    print('Aprovado!')
else:
    print('Recuperação!')


print(f'Média final: {media:.2f}')