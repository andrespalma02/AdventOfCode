f = open("particip.txt", "r")
lista = []
cont = 0
for line in f:
    if cont % 4 == 0:
        lista.append(line.rstrip("\n"))
    cont += 1
dic = {}
for item in lista:
    dic[item] = dic.get(item, 0) + 1

for k in dic:
    print(k,": ",dic[k])
