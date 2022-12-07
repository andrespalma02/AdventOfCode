f = open("input.txt", "r")
rec = list()
for line in f:
    line = ' '.join(line.split())
    rec.append(list(map(int, line.split(" "))))
con = 0
div = 0
for num in rec:
    for i in num:
        for j in num:
            if (i % j == 0) and (i != j):
                div += i / j
    con += max(num) - min(num)
print(con)
print(int(div))
