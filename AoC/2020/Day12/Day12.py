f = open("input.txt", "r")
# Definimos las variables
EW = 0
NS = 0
dir = 90

for line in f:
    action = line[0]  # accion de la coordenada
    num = int(line[1:])
    if action == "F" and dir == 90 or action == "E":
        EW += num
    elif action == "F" and dir == 180 or action == "S":
        NS -= num
    elif action == "F" and dir == 270 or action == "W":
        EW -= num
    elif action == "F" and dir == 0 or action == "N":
        NS += num
    elif action == "L":
        dir -= num
        if dir == 360 or dir == -360:
            dir = 0
        if dir == -90:
            dir = 270
        if dir == -180 or dir == 540:
            dir = 180
        if dir == -270 or dir == 450:
            dir = 90

    elif action == "R":
        dir += num
        if dir == 360 or dir == -360:
            dir = 0
        if dir == -90:
            dir = 270
        if dir == -180 or dir == 540:
            dir = 180
        if dir == -270 or dir == 450:
            dir = 90
print("PRIMERA PARTE")
print(f"Distancia a Manhattan: {abs(NS) + abs(EW)}")

ship_ew = 0
ship_ns = 0
way_ew = 10
way_ns = 1
f = open("input.txt", "r")
for line in f:
    action = line[0]
    num = int(line[1:])

    if action == "F":
        ship_ns += (way_ns * num)
        ship_ew += (way_ew * num)
    elif action == "N":
        way_ns += num
    elif action == "S":
        way_ns -= num
    elif action == "E":
        way_ew += num
    elif action == "W":
        way_ew -= num

    elif action == "L" and num == 90 or action == "R" and num == 270:
        way_ns, way_ew = way_ew, -way_ns
    elif action == "L" and num == 270 or action == "R" and num == 90:
        way_ns, way_ew = -way_ew, way_ns
    elif action == "L" and num == 180 or action == "R" and num == 180:
        way_ns = -way_ns
        way_ew = -way_ew
print()
print("SEGUNDA PARTE")
print(f"Distancia a Manhattan: {abs(ship_ns) + abs(ship_ew)}")
