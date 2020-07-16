pri = int(input("Digite o primeiro termo: "))
sec = int(input("Digite o segundo termo: "))

for c in range(pri,11,sec):
    print("{}".format(c), end=' -> ')
print("\033[34mFIM\033[m")
