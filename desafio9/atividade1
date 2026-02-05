print('--SISTEMA DE CADASTRO DE ALUNOS--')
#LISTA PARA ARMAZENAR OS CADASTROS
cadastro_alunos = []
#PEÇO A INFORMAÇÃO DE QUANTOS ALUNOS PODEM SER CADASTRADOS
quantidade_de_alunos = int(input('Quantos alunos podem ter nessa turma? '))
#CRIEI O FOR PARA A REPETIÇÃO DE QUANTAS VEZES IREMOS CADASTRAR OS ALUNOS
for i in range(quantidade_de_alunos):
    print(f"\nCadastrando aluno {i + 1}")
    aluno = {} #OPTEI POR ARMAZENAR AS INFORMÇÕES DOS ALUNOS NUM DICIONARIO POIS PRECISAREI ASSOCIAR AS NOTAS, A MEDIA E A SITUÇÃO
    aluno['nome'] = input("Digite o nome do aluno: ")
#AQUI CRIEI UMA LISTA PARA ARMAZER AS 3 NOTAS
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    aluno['notas'] = notas #ADICIONA A NOTA A LISTA NOTAS
#PARA CAUCULAR A MEDIA E CRIAR A SITUÇÃO DENTRO DO DICIONARIO
    media = sum(notas) / len(notas)
    aluno['media'] = media

    if media >= 7:
        aluno['situacao'] = 'Aprovado'
    elif media >= 4:
        aluno['situacao'] = 'Recuperação'
    else:
        aluno['situacao'] = 'Reprovado'

    cadastro_alunos.append(aluno) #ADICIONO AS INFORMAÇÕES DO ALUNO NA MINHA LISTA DE CADASTRO
#IMMPRIMO O REULTADO
print("\nAlunos cadastrados")
for aluno in cadastro_alunos:
    print("Nome:", aluno['nome'])
    print("Notas:", aluno['notas'])
    print("Média:", aluno['media'])
    print("Situação:", aluno['situacao'])
    print("\n")