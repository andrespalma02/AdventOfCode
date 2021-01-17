import re

invalid = list()
for i in range(1000):
    invalid.append(i)
f = open("inputejm.txt", "r")
rules = dict()
my_ticket = ""
tickets = list()
flag = 1
# se dividen los tickets validos, el ticket propio, y las reglas
for line in f:
    if line == "\n":
        flag += 1
    if flag == 1:
        k, v = line.replace("\n", "").split(":")
        rules[k] = v.split("or")
    if flag == 2:
        my_ticket = line
    if flag == 3 and (not line.startswith("n")):
        tickets.append(line.replace("\n", ""))
tickets.pop(0)

# se crea la lista de numeros invalidos
for k, v in rules.items():
    num1, num2 = v[0].split("-")
    for i in range(int(num1), int(num2) + 1):
        if i in invalid:
            invalid.remove(i)
    num1, num2 = v[1].split("-")
    for i in range(int(num1), int(num2) + 1):
        if i in invalid:
            invalid.remove(i)
# se verifican los tickets invalidos
suma = 0
laux = list()
flag = False
for i in range(len(tickets)):
    laux = tickets[i].split(",")
    for num in laux:
        if int(num) in invalid:
            suma += int(num)
            flag = True
    if flag:
        tickets[i] = ""
        flag = False
print(suma)
tickets = list(filter(None, tickets))

for k,v in rules.items():
    num1, num2 = v[0].split("-")
    num3, num4 = v[1].split("-")


