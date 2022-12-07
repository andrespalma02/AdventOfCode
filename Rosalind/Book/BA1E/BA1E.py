def clump_finding(genome, k, L, t):
    clump = []
    for i in range(len(genome) - L + 1):
        window = genome[i:i + L]
        for j in range(len(window) - k + 1):
            pattern = window[j:j + k]
            count = window.count(pattern)
            if count >= t and pattern not in clump:
                clump.append(pattern)
    print(len(genome))
    return clump


with open("rosalind_ba1e.txt") as file:
    gen = file.readline().strip()
    k, L, t = map(int, file.readline().strip().split())
    print(" ".join(clump_finding(gen, k, L, t)))
