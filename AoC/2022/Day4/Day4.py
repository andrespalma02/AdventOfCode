def day_4_1_2022(file):
    pairs = 0
    for line in file.read().strip().split("\n"):
        [section1, section2] = line.split(",")
        [section1_min, section1_max] = map(int, section1.split("-"))
        [section2_min, section2_max] = map(int, section2.split("-"))
        if section2_min <= section1_min <= section1_max <= section2_max\
                or section1_min <= section2_min <= section2_max <= section1_max:
            pairs += 1
    print(pairs)


def day_4_2_2022(file_2):
    pairs = 0
    for line in file_2.read().strip().split("\n"):
        [section1, section2] = line.split(",")
        [section1_min, section1_max] = map(int, section1.split("-"))
        [section2_min, section2_max] = map(int, section2.split("-"))
        if section2_min <= section1_min <= section1_max <= section2_max\
                or section1_min <= section2_min <= section2_max <= section1_max\
                or section1_min <= section2_min <= section1_max <= section2_max\
                or section2_min <= section1_min <= section2_max <= section1_max:
            pairs += 1
    print(pairs)


with open("input.txt", "r") as file:
    day_4_1_2022(file)
    with open("input.txt", "r") as file_2:
        day_4_2_2022(file_2)
