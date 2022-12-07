def pattern_occurrences(pattern, text):
    positions = []
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions


with open("rosalind_ba1d.txt") as file:
    print(" ".join(str(i) for i in pattern_occurrences(file.readline().strip(), file.readline().strip())))

