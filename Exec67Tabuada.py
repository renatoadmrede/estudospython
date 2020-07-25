n1 = 0
count = 0
resultado = 0
valor = 0
while True:
    n1 = int(input('Quer ver a tabuada de qual valor?: '))
    if n1 < 0:
        break
    for count in range(1,11):
        resultado = n1 * count
        print(f'{n1} x {count} = {resultado}')
print('FIM')