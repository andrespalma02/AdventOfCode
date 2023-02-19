import time


def day_6_1_2021(file):
    days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    fishes = list(map(int, file.read().split(",")))
    for fish in fishes:
        days[fish] += 1
    for i in range(500):
        aux = days[0]
        for j in range (8):
            days[j] = (days[j + 1] if j != 6 else days[j + 1] + aux)
        days[8] = aux
    print(sum(day for day in days.values()))


def day_6_2_2021(file_2):
    pass


if __name__ == "__main__":
    file = open("input.txt", "r")
    start = time.time()
    day_6_1_2021(file)
    end = time.time()
    print("Time:", end - start)

    file_2 = open("input.txt", "r")
    day_6_2_2021(file_2)
