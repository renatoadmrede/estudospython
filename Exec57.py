sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Vc digitou errado. Digite novamente: ".format())).strip().upper()[0]
print("O sexo {} foi cadastrado".format(sexo))

