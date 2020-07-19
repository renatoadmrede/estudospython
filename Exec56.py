somaidade = 0
maioridade = 0
homemidade = ''
countm = 0
for p in range(1,5):
    print("----- {}ª PESSOA -----".format(p))
    nome = str(input("NOME: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    somaidade = idade + somaidade
    if p == 1 and sexo in 'mM':
        maioridade = idade
        homemidade = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        homemidade = nome
    if idade < 20 and sexo in 'fF':
        countm = countm + 1

mediaidade = somaidade / 4
print("A média de idade é {}".format(mediaidade))
print("O home mais velho é {} que tem {} anos".format(homemidade, maioridade))
print("Existem {} mulheres com menos de 20 anos".format(countm))
