f = open("input.txt", "r")
listaboletos = list()
for line in f:
    listaboletos.append(line.replace("\n", ""))
ids = list()
for boleto in listaboletos:
    minF = 0
    maxF = 127
    minC = 0
    maxC = 7
    for letra in boleto:
        if letra == "F":
            maxF = int((minF + maxF) / 2)
        if letra == "B":
            minF = int((minF + maxF) / 2) + 1
        if letra == "R":
            minC = int((minC + maxC) / 2) + 1
        if letra == "L":
            maxC = int((minC + maxC) / 2)
    ids.append((maxF * 8) + maxC)
ids = sorted(ids, reverse=True)
print("El ID mas alto es: ", ids[0])
for i in range(len(ids) - 1):
    if (ids[i] - ids[i + 1]) > 1:
        print("El ID de mi asiento es: ", int((ids[i] + ids[i + 1]) / 2))