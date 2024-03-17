f = open("rosalind_ba1g.txt", "r")


# hamming distance between two strings
def hamming_distance(s1, s2):
    return sum([1 for x, y in zip(s1, s2) if x != y])


s1 = f.readline().strip()
s2 = f.readline().strip()
print(hamming_distance(s1, s2))