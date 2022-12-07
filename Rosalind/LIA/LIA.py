def independent_alleles(k, N):
    m = 2 ** k
    p = 0.5 ** k


with open("C:/Users/Pc/PycharmProjects/rosalind/LIA/rosalind_lia.txt") as file:
    a, b = file.readline().strip().split()
    print(independent_alleles(int(a), int(b)))
