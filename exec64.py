cont = 0
soma = 0
valor = int(input("Digite um valor (999 para sair): "))
while valor != 999:
    cont = cont + 1
    soma = soma + valor
    valor = int(input("Digite um valor (999 para sair): "))
print('A soma dos {} valores foi {}'.format(cont,soma))
print('Fim')













'''n = 0
count = -1
soma = 0
n = int(input("Digite 999 para parar: "))
while n != 999:
    soma = soma + n
    count = count + 1
    n = int(input("Digite 999 para parar: "))
print("Vc digitou {} números e a soma entre eles foi {}".format(count,soma))'''