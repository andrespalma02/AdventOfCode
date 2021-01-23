f = open("input1.txt", "r")
mass = list()
tot = 0


def recsum(mass):
    if mass <= 0:
        return 0
    else:
        suma = int(int(mass) / 3) - 2
        print(suma)
    return mass + recsum(suma)


for line in f:
    mass.append(int(int(line) / 3) - 2)
print(sum(mass))
for m in mass:
    tot += recsum(m)
print(tot)
