f = open("input25.txt", "r")

door_pk = int(f.readline().strip())
card_pk = int(f.readline().strip())

door_loop = 0
card_loop = 0
aux = 1
while aux != door_pk:
    aux = (7 * aux) % 20201227
    door_loop += 1
print(door_loop)
aux = 1
while aux != card_pk:
    aux = (7 * aux) % 20201227
    card_loop += 1
print(card_loop)

encrypted1 = 1
for i in range(door_loop):
    encrypted1 = (encrypted1 * card_pk) % 20201227
encrypted2 = 1
for i in range(card_loop):
    encrypted2 = (encrypted2 * door_pk) % 20201227

print(encrypted1, encrypted2)
