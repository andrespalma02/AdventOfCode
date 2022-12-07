f = open("input.txt")
lis_num = list()
inv_num = 0
ind = 0
for line in f:
    lis_num.append(int(line.replace("\n", "")))


def verificar(num, lista):
    for i in lista:
        if num - i in lista:
            return True


for i in range(25, len(lis_num)):
    if not verificar(lis_num[i], lis_num[i - 25: i]):
        inv_num = lis_num[i]
        ind = i
        print(inv_num, i)
listasum = list()
for i in range(ind):
    suma = 0
    sus = list()
    for j in range(i, ind):
        if suma < inv_num:
            sus.append(lis_num[j])
            suma += lis_num[j]
        elif suma == inv_num:
            sus.sort()
            listasum = sus
            suma = 0
            sus = list()
            break
suma = listasum[0] + listasum[-1]
print(suma)
