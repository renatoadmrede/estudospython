print('---'*20)
print('                    LOJA SUPER BARATÃO')
print('---'*20)
preco = 0
total = 0
count1000 = 0
countmen = 0

while True:
    produto = ' '
    produto = str(input('Nome do pruduto: '))
    preco = float(input('Preço: R$ '))
    total = preco + total
    if preco > 1000:
        count1000 = count1000 + 1
    menor = preco
    if preco < menor:
        menor = preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi {total}')
print(f'Temos {count1000} custando mais de R$ 1000.00')
print(f'O produto mais barato custou {menor}')
print('--------------- FIM DO PROGRAMA ---------------')


