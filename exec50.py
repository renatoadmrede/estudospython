soma = 0
for c in range(1,7):
    c = int(input("Digite um número: "))
    if c % 2 == 0:
        soma = c + soma
print("O resultado da soma é {}: ".format(soma))