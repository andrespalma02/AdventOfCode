f = open("rosalind_ba1h.txt", "r")

# find all approximate occurrences of a pattern in a string
def approximate_pattern_matching(text, pattern, d):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if sum([1 for x, y in zip(text[i:i + len(pattern)], pattern) if x != y]) <= d:
            positions.append(i)
    return positions


pattern = f.readline().strip()
text = f.readline().strip()
d = int(f.readline().strip())
print(" ".join(map(str, approximate_pattern_matching(text, pattern, d))))