num = int(input("Digite um número: "))
count = 0
count2 = 0
for c in range(1,num+1):
    if num % c == 0:
        print("\033[34m", end='')
        count = count + 1
    else:
        print("\033[35m", end='')
   # print("{}".format(c))
print("O numero {} foi dividio {} vezes".format(num,count))
if count == 2:
    print("{} é Primo".format(num))
else:
    print("{} N é Primo".format(num))