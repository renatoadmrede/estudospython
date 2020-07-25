soma = 0
cont = 0
valor = 0
while True:
    valor = int(input('Digite um valor (999 para sair)'))
    if valor == 999:
        break
    soma = soma + valor
    cont = cont + 1
print(f'A soma dos {cont} números inseridos é {soma}')
