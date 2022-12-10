def day_6_1_2022(file):
    file = file.read()
    for i in range(len(file) - 4):
        if len(file[i:i + 4]) == len(set(file[i:i + 4])):
            print(i + 4)
            break


def day_6_2_2022(file):
    file = file.read()
    for i in range(len(file) - 14):
        if len(file[i:i + 14]) == len(set(file[i:i + 14])):
            print(i + 14)
            break


with open("input.txt", "r") as file:
    day_6_1_2022(file)
    with open("input.txt", "r") as file:
        day_6_2_2022(file)
