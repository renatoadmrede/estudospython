c = ('zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove',
           'Dez','onze','doze')

while True:
    numero = int(input('Digite um número:'))
    if 0 <= numero <= 12:
        print(f'Vc digitou: {c[numero]}')
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Vc quer continuar? ')).upper().strip()[0]
    if escolha == 'N':
        break
print('FIM')





