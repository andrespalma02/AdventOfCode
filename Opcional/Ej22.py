f = open("inputejm.txt", "r")
flag = True
dock2 = list()
dock1 = list()
# se añade del input a los docks
for line in f:
    line = line.replace("\n", "")
    if line.startswith("Player 2:"):
        flag = False
    if line.isdigit():
        if flag:
            dock1.append(int(line))
        else:
            dock2.append(int(line))
ronda = 0
while (len(dock1) != 0) & (len(dock2) != 0):
    ronda += 1
    if dock2[0] > dock1[0]:
        dock2.append(dock2[0])
        dock2.append(dock1[0])
        dock1.pop(0)
        dock2.pop(0)
    else:
        dock1.append(dock1[0])
        dock1.append(dock2[0])
        dock1.pop(0)
        dock2.pop(0)
i = 0
score = 0
if len(dock1) > len(dock2):
    for card in reversed(dock1):
        i += 1
        score += card * i
else:
    for card in reversed(dock2):
        i += 1
        score += card * i
print(score)
