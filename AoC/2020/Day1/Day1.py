# abrir el archivo
f = open("input.txt", "r")
lis_num = list()
# guardamos cada número en una lista con ENTERO
for line in f:
    lis_num.append(int(line))
# itero en la lista
for num in lis_num:
    if (2020 - num) in lis_num:
        print(num, 2020 - num, (2020 - num) * num)
        break
# itero en la lista
for num1 in lis_num:
    for num2 in lis_num:
        if (2020 - num1 - num2) in lis_num:
            print(num1, num2, (2020 - num1 - num2), num1 * num2 * (2020 - num1 - num2))
            break
