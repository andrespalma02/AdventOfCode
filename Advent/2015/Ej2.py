from math import prod

f = open("input2.txt", "r")
gift = list()
area = list()
rib = list()
for line in f:
    gift.append(list(map(int, line.replace("\n", "").split("x"))))
for line in gift:
    rib.append(2 * (sorted(line)[0] + sorted(line)[1]) + prod(line))
    a1 = line[0] * line[1]
    a2 = line[0] * line[2]
    a3 = line[1] * line[2]
    area.append(2 * (a1 + a2 + a3) + min(a1, a2, a3))
print(sum(area))
print(sum(rib))
