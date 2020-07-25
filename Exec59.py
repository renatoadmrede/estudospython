from time import sleep
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
opcao = 0

while opcao !=5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR''')
    opcao = int(input(">>> Qual a sua opção <<<? "))
    if opcao == 1:
        soma = n1 + n2
        print('\033[31mO resultado da soma é {}\033[m'.format(soma))
    elif opcao == 2:
        mult = n1 * n2
        print('\033[32mO resultado da multiplicação é {}\033[m'.format(mult))
    elif opcao == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1,n2))
        else:
            print("{} é maior que {}".format(n2,n1))
    elif opcao == 4:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif opcao == 5:
        print("Obrigado!!!...")
        sleep(2)
    else:
        print("Opção errada")
        sleep(2)
