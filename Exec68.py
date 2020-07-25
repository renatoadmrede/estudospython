from random import randint

v = 0
valor = 0
soma = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-'*20)

while True:
    comp = randint(1, 10)
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]'))
    soma = comp + valor
    if soma % 2 == 0:
        print(f'Vc jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
        if escolha in 'P':
            print('VC VENCEU')
            v = v + 1
        else:
            print('VC PERDEU')
            break
    elif soma % 2 == 0:
        print(f'Vc jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
        if escolha in 'I':
            print('VC VENCEU')
            v = v + 1
        else:
            print('VC PERDEU')
            break
    elif soma % 2 != 0:
        print(f'Vc jogou {valor} e o computador {comp}. Total de {soma} DEU IMPAR')
        if escolha in 'P':
            print('VC PERDEU')
            break
        else:
            print('VC VENCEU')
            v = v + 1
    elif soma % 2 != 0:
        print(f'Vc jogou {valor} e o computador {comp}. Total de {soma} DEU IMPAR')
        if escolha in 'I':
            print('VC VENCEU')
            v = v + 1
        else:
            print('VC PERDEU')
            break
    print(f"Vc ganhou {v} vezes!!!")
print('GAME OVER!!!!!!')


