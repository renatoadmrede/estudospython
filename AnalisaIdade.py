from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,7):
    idade = int(input("Em que ano a {}ª nasceu? ".format(c)))
    idade = atual - idade
    if idade < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print("Menorr idade temos {}".format(menor))
print("Maior idade temos {}".format(maior))




