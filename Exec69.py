idade = 0
total18 = 0
totalM = 0
totalF20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        total18 = total18 + 1
    if sexo == 'M':
        totalM = totalM + 1
    if sexo == 'F' and idade < 20:
        totalF20 = totalF20 + 1
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('Deseja cadastrar outra pessoaw: ')).strip().upper()
    if escolha == 'N':
        break

print(f'O total de pessoas com mais de 18 anos é: {total18}')
print(f'O total de Homens é: {totalM}')
print(f'O total de mulheres com menos de 20 anos é: {totalF20}')