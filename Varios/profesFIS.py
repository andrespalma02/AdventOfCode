doc = open("new1.txt", "r", encoding='utf8')
lista = []
for line in doc:
    if line.startswith("Teacher"):
        lista.append(line.rstrip().lstrip("Teacher: "))


for i in range(len(lista)):
    lista2 = lista[i].split()
    lista[i] = lista2[-2] + " " + lista2[-1] + " " + lista2[0] + " " + lista2[1]
setunico = sorted(set(lista))
doc2 = open("profes.txt", "w")
for item in setunico:
    doc2.write(item + "\n")
