f = open("input3.txt", "r")
rec = list()
for line in f:
    line = ' '.join(line.split())
    rec.append(list(map(int, line.split(" "))))
aux = list()
flag = 1
con = 0
for i in range(len(rec[0])):
    for j in range(len(rec)):
        aux.append(rec[j][i])
        aux = sorted(aux)
        if flag % 3 == 0:
            print(aux)
            if (aux[0] + aux[1]) > aux[2]:
                con += 1
            aux = list()
        flag += 1
print(con)
con = 0
for el in rec:
    el = sorted(el)
    if (el[0] + el[1]) > el[2]:
        con += 1
print(con)
