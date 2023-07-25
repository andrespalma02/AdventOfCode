from Bio import SeqIO
from Bio.Seq import Seq

# read in the DNA string and introns from the FASTA file
records = list(SeqIO.parse("rosalind_splc.fasta", "fasta"))
for record in records:
    print(record, "\n")
dna_seq = str(records[0].seq)
print("Secuencia: ", dna_seq, "\n")
introns = [str(record.seq) for record in records[1:]]
print("Intrones: ", introns, "\n")

# remove the introns from the DNA string
for intron in introns:
    dna_seq = dna_seq.replace(intron, "")
    print("Secuencia recortada: ", dna_seq, "\n")

# transcribe the DNA sequence to mRNA
mRNA_seq = Seq(dna_seq).transcribe()
print("Secuencia de mRNA: ", mRNA_seq, "\n")

# translate the mRNA sequence to protein
protein_seq = mRNA_seq.translate(to_stop=True)

# print the resulting protein string
print(protein_seq)
