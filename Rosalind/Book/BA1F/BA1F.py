def minimize_skew(genome):
    skew = [0]
    for i in range(len(genome)):
        if genome[i] == 'G':
            skew.append(skew[i] + 1)
        elif genome[i] == 'C':
            skew.append(skew[i] - 1)
        else:
            skew.append(skew[i])
    min_skew = min(skew)
    return [i for i in range(len(skew)) if skew[i] == min_skew]


with open("rosalind_ba1f.txt") as file:
    print(" ".join(str(i) for i in minimize_skew(file.readline().strip())))
