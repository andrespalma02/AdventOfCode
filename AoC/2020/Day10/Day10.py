f = open("input.txt", "r")
lista_jolts = list()
for jolt in f:
    lista_jolts.append(int(jolt.replace("\n", "")))
lista_jolts.sort()
dif1 = 0
dif2 = 0
dif3 = 0
for i in range(len(lista_jolts) - 1):
    if (lista_jolts[i + 1] - lista_jolts[i]) == 1:
        dif1 += 1
    if (lista_jolts[i + 1] - lista_jolts[i]) == 2:
        dif2 += 1
    if (lista_jolts[i + 1] - lista_jolts[i]) == 3:
        dif3 += 1
print(dif1 + 1, " diferencias de 1 jolt y ", dif3 + 1, " diferencias de 3 jolts")
print("El producto de estas diferencias es", (dif1 + 1) * (dif3 + 1))

dic_jolt = {0: 1}
for jolt in lista_jolts:
    dic_jolt[jolt] = dic_jolt.get(jolt - 1, 0) + dic_jolt.get(jolt - 2, 0) + dic_jolt.get(jolt - 3, 0)
print("Las combinaciones posibles son: ", dic_jolt[max(lista_jolts)])
