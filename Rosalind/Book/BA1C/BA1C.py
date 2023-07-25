from Bio.Seq import reverse_complement

with open("rosalind_ba1c.txt") as file:
    print(reverse_complement(file.readline().strip()))
