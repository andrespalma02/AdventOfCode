f = open("in.txt", "r")

lines = str(f.readline()).split(" ")

words_freq = {}

for line in lines:
    words_freq[line] = words_freq.get(line, 0) + 1

for key, value in words_freq.items():
    print(f"{key} {value}")
