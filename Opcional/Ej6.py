f = open("input6.txt", "r")
data = f.read().split("\n\n")
lista = list()
# todos los datos en una sola linea
lis_al = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

for line in data:
    lista.append("".join(set(line.replace("\n", ""))))
con = 0
for line in lista:
    con += len(line)
print(con)

laux = list()
con2 = 0
for line in data:
    laux = line.split("\n")
    for letter in lis_al:
        correct = 0
        for elem in laux:
            if letter in elem:
                correct += 1
        if correct == len(laux):
            con2 += 1
print(con2)
