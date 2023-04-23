import itertools

f = open("C:/Users/Pc/PycharmProjects/rosalind/PERM/rosalind_perm_output.txt", "w")


def permute(n):
    nums = [i for i in range(1, int(n) + 1)]
    perm = list(itertools.permutations(nums))
    f.write(str(len(perm)) + "\n")
    print(len(perm))
    for i in perm:
        i = [str(j) for j in list(i)]
        print(" ".join(i))
        f.write(" ".join(i) + "\n")
    f.close()


with open("C:/Users/Pc/PycharmProjects/rosalind/PERM/rosalind_perm.txt") as file:
    s = file.readline().strip()
    permute(s)
