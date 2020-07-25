count = 1
mais = 5
total = 0

print('-='*10)
print('GERADOR DE PA')
print('-='*10)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input('Digite a Razão: '))

while mais != 0:
    total = mais + total
    while count <= total:
        print('{} ->'.format(primeiro), end='')
        primeiro = razao + primeiro
        count = count + 1
    print(' PAUSA')
    mais = int(input('Quantos termos a mais vc quer? '))
print(' FIM')

