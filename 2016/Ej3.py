f = open("input3.txt", "r")
rec = list()
for line in f:
    line = ' '.join(line.split())
    rec.append(list(map(int, line.split(" "))))
con = 0
for el in rec:
    el = sorted(el)
    if (el[0] + el[1]) > el[2]:
        con += 1
print(con)
