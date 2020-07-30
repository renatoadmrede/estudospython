media = 0
aprovados = 0
reprovados = 0
final = 0
while True:
    print('=' * 60)
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    print('=' * 60)
    media = (nota1 + nota2) / 2

    if media <= 4:
        reprovados = reprovados + 1
    if media > 4 and media < 7:
        final = final + 1
    if media > 7:
        aprovados = aprovados + 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja ver o resultado da média? ')).strip().upper()[0]
    if resposta == 'S':
        print('=' * 60)
        print(f'O resultado da média do aluno {aluno} é {media}.')
        print(f'Temos {aprovados} alunos aprovados, {final} alunos indo pra final e {reprovados} alunos reprovados')

        resposta2 = ' '
        while resposta2 not in 'SN':
            resposta2 = str(input('Deseja continuar com o cadastro? ')).strip().upper()[0]
        if resposta2 == 'N':
            break


print('Fim de cadastro de notas...')



'''media = 0
aprovados = 0
reprovados = 0
final = 0
while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2

    if media <= 4:
        reprovados = reprovados + 1
    if media > 4 and media < 7:
        final = final + 1
    if media > 7:
        aprovados = aprovados + 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja ver o resultado da média? ')).strip().upper()[0]
    if resposta == 'N':
        break

    print(f'O resultado da média do aluno {aluno} é {media}.')
    print(f'Temos {aprovados} alunos aprovados, {final} alunos indo pra final e {reprovados} alunos reprovados')

    resposta2 = ' '
    while resposta2 not in 'SN':
        resposta2 = str(input('Deseja continuar com o cadastro')).strip().upper()[0]
    if resposta2 == 'N':
        break
print('Fim de cadastro de notas...')'''