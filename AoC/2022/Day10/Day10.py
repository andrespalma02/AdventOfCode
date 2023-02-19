def day_10_1_2022(file):
    cont = 0
    value = 1
    for line in file:
        if line.startswith("noop"):
            cont += 1
        else:
            cont += 2
            value += int(line.lstrip("addx "))
            print(cont, value)


def day_10_2_2022(file_2):
    pass


with open('inputt.txt') as file:
    day_10_1_2022(file)
    with open('inputt.txt') as file_2:
        day_10_2_2022(file_2)
