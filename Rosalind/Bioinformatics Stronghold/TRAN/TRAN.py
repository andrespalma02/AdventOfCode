from Bio import SeqIO
from Bio.Seq import Seq

# read in the DNA string and introns from the FASTA file
records = list(SeqIO.parse("rosalind_tran.fasta", "fasta"))
for record in records:
    print(record, "\n")
seq1 = str(records[0].seq)
seq2 = str(records[1].seq)

transitions = 0
transversions = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        if (seq1[i] == "A" and seq2[i] == "G") or (seq1[i] == "G" and seq2[i] == "A") or (
                seq1[i] == "C" and seq2[i] == "T") or (seq1[i] == "T" and seq2[i] == "C"):
            transitions += 1
        else:
            transversions += 1

print(transitions/transversions)


"""
optimal
def transitionTransversionRatio(s1, s2):
    trans = {"A":"G", "G":"A", "T":"C", "C":"T"}
    mut = [0 if trans[b1] == b2 else 1 for b1, b2 in zip(s1,s2) if b1 is not b2]
    return mut.count(0) / float(mut.count(1))
"""