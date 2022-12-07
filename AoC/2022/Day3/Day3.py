def day_3_1_2022(file):
    add = 0
    for line in file.read().strip().split("\n"):
        half = int(len(line) / 2)
        common = (set(line[:half]) & set(line[half:])).pop()
        add += ord(common) - 96 if common.islower() else ord(common) - 38
    print(add)


def day_3_2_2022(file_2):
    add = flag = 0
    lines = []
    for line in file_2.read().strip().split("\n"):
        lines.append(line)
        if flag <= 1:
            flag += 1
        else:
            letter = (set(lines[0]) & set(lines[1]) & set(lines[2])).pop()
            add += ord(letter) - 96 if letter.islower() else ord(letter) - 38
            lines = []
            flag = 0
    print(add)


with open("input.txt", "r") as file:
    day_3_1_2022(file)
    with open("input.txt", "r") as file_2:
        day_3_2_2022(file_2)
