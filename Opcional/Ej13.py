f = open("inputejm.txt", "r")
lis = list()
for line in f:
    lis.append(line.replace("\n", ""))
timestamp = int(lis[0])
lis = lis[1].split(",")
buses = list()
for item in lis:
    if item != "x":
        buses.append(int(item))
print(buses, timestamp)
found = False
aux = timestamp
id_bus = 0
while not found:
    for bus in buses:
        if int(aux) % int(bus) == 0:
            id_bus = bus
            found = True
    aux += 1
aux -= 1
print(aux, id_bus, (aux - timestamp) * id_bus)
