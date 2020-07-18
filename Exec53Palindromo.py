frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if junto == inverso:
    print("{} e {} são palídromos".format(inverso,junto))
else:
    print("{} e {} não são palídromos".format(inverso,junto))