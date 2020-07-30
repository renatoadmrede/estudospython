valor = int(input('Quanto vc quer sacar? '))
count1 = count10 = count20 = count50 = 0
while True:

    if valor >= 50:
        valor = valor - 50
        count50 = count50 + 1
    elif valor >= 20:
        valor = valor - 20
        count20 = count20 + 1
    elif valor >= 10:
        valor = valor - 10
        count10 = count10 + 1
    elif valor >= 1:
        valor = valor - 1
        count1 = count1 + 1
    else:
        break
if count1 > 0:
    print(f'Vc pegou {count1} notas de 1 Reais')
if count10 > 0:
    print(f'Vc pegou {count10} notas de 10 Reais')
if count20 > 0:
    print(f'Vc pegou {count20} notas de 20 Reais')
if count50 > 0:
    print(f'Vc pegou {count50} notas de 50 Reais')




'''valor = int(input('Quanto vc quer sacar? '))
count1 = count10 = count20 = count50 = 0
while True:

    if valor >= 50:
        valor = valor - 50
        count50 = count50 + 1
    elif valor >= 20:
        valor = valor - 20
        count20 = count20 + 1
    elif valor >= 10:
        valor = valor - 10
        count10 = count10 + 1
    elif valor >= 1:
        valor = valor - 1
        count1 = count1 + 1
    else:
        break
print(f'Vc pegou {count1} notas de 1 Reais')
print(f'Vc pegou {count10} notas de 10 Reais')
print(f'Vc pegou {count20} notas de 20 Reais')
print(f'Vc pegou {count50} notas de 50 Reais')
'''
