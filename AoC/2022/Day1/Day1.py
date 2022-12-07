def day_1_1_2022(file):
    data = max(
        [
            sum(
                list(
                    map(
                        int, item.split()
                    )
                )
            )
            for item in file.read().split("\n\n")
        ]
    )
    print(data)


def day_1_2_2022(file_2):
    data = sum(
        sorted(
            [
                sum(
                    list(
                        map(
                            int, item.split()
                        )
                    )
                )
                for item in file_2.read().split("\n\n")
            ], reverse=True
        )[:3]
    )
    print(data)


with open("input.txt", "r") as file:
    day_1_1_2022(file)
    with open("input.txt", "r") as file:
        day_1_2_2022(file)

