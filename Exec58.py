from random import randint
count = 0
ran = randint(0,10)
num = ''

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que vc consegue adivinhar qual foi?''')

while num != ran:
    num = int(input("Qual o seu palpite?: "))
    if num > ran:
        print("Digite menor...Tente denovo")
    elif num < ran:
        print("Digite Maior...Tente denovo")
    count = count + 1
print("Acertou com {}  tentativas. Parabéns.".format(count))
