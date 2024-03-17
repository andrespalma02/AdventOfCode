from Bio import Entrez
from Bio import SeqIO
f = open("D:\GitKraken\AdventOfCode\Rosalind\Bioinformatics Armory\FRMT\\rosalind_frmt.txt", "r")
ids = f.readline().strip().split()
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
min_id = min(records, key=lambda x: len(x.seq))

handle = Entrez.efetch(db="nucleotide", id=min_id.id, rettype="fasta")
records = handle.read()
print(records)