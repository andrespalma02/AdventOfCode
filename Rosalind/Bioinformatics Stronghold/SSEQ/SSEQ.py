# No sirve, corregir

from Bio import SeqIO

# read the input file containing s and t in FASTA format
records = list(SeqIO.parse("rosalind_sseq.fasta", "fasta"))
s = records[0].seq
t = records[1].seq

# find all the indexes of t as a subsequence of s
indexes = []
j = 0
for i in range(len(s)):
    if s[i] == t[j]:
        j += 1
        if j == len(t):
            indexes.append(i-len(t)+2)
            j = 0

# print the indexes
print(indexes)