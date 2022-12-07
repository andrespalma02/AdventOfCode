def day2_1_2019(data):
    data = [int(i) for i in data.readline().split(",")]
    data[1] = 12
    data[12] = 2
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        elif data[i] == 99:
            break
    return data[0]


def day2_2_2019(data):
    data = [int(i) for i in data.readline().split(",")]
    for noun in range(100):
        for verb in range(100):
            data[1] = noun
            data[2] = verb
            for i in range(0, len(data), 4):
                if data[i] == 1:
                    data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
                elif data[i] == 2:
                    data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
                elif data[i] == 99:
                    break
            if data[0] == 19690720:
                return 100 * noun + verb
            data = [int(i) for i in data]


if __name__ == '__main__':
    with open('input.txt') as file:
        print(day2_1_2019(file))
        with open('input.txt') as file:
            print(day2_2_2019(file))
