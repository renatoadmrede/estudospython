from datetime import date
atual = date.today().year
count = 0
count2 = 0
for p in range(1,6):
    ano = int(input("Em que ano a {}ª pessoa nasceu: ".format(p)))
    idade = atual - ano
    if idade >= 18:
        count = count + 1
    else:
        count2 = count2 + 1
print("Ao todo temos {} pessoas de moiar".format(count))
print("E temos {} pessoas de menor".format(count2))

