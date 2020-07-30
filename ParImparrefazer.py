from random import randint
jogadornum = 0
computdor = 0
soma = 0
while True:
    jogadornum = int(input('Digite um número: '))
    jogadorpi = ' '
    while jogadorpi not in 'PI':
        jogadorpi = str(input('PAR ou IMPAR? [P/I')).strip().upper()[0]
    computador = randint(0,10)
    soma = computador + jogadornum
    print(f'Vc jogou {jogadornum} e o computador jogou {computador} o número é: {soma}')
    if soma % 2 == 0 and jogadorpi == 'P':
        print(f'Vc venceu. Jogou {jogadorpi} ')
    elif soma % 2 == 0 and jogadorpi == 'I':
        print(f'Vc perdeu. Jogou {jogadorpi} ')
        break
    elif soma % 2 == 1 and jogadorpi == 'I':
        print(f'Vc venceu. Jogou {jogadorpi} ')
    elif soma % 2 == 1 and jogadorpi == 'P':
        print(f'Vc perdeu. Jogou {jogadorpi} ')
        break
print('GAME OVER!!!')