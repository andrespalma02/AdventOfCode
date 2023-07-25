# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import os

from Bio import SeqIO
from Bio.Align.Applications import MafftCommandline
from Bio.Align.Applications import MuscleCommandline
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# -
# ## Genome alignment

"""
mafft_cline = MafftCommandline(cmd="C:\MAFFT\mafft.bat", input='sample.fasta', ep=0.345, maxiterate=10)
print(mafft_cline)
stdout, stderr = mafft_cline()
print(stdout)
with open('align.fasta', 'w') as w:
    print('XX')
    w.write(stdout)
"""



os.system('trimal -automated1 -in D:\GitKraken\AdventOfCode\AlgoritmosBio\Proyecto\\align.fasta -out D:\GitKraken\AdventOfCode\AlgoritmosBio\Proyecto\\trim.fasta -fasta')

# ## Protein alignment

# +


my_genes = ['NP', 'L', 'VP35', 'VP40']

"""
for gene in my_genes:
    muscle_cline = MuscleCommandline( input='%s_P.fasta' % gene)
    print(muscle_cline)
    stdout, stderr = muscle_cline()
    with open('%s_P_align.fasta' % gene, 'w') as w:
        w.write(stdout)

"""

# +

# XXX vvv
#from Bio.Alphabet import generic_protein

for gene in my_genes:
    gene_seqs = {}
    unal_gene = SeqIO.parse('%s.fasta' % gene, 'fasta')
    for rec in unal_gene:
        gene_seqs[rec.id] = rec.seq

    al_prot = SeqIO.parse('%s_P_align.fasta' % gene, 'fasta')
    al_genes = []
    for protein in al_prot:
        my_id = protein.id
        seq = ''
        pos = 0
        for c in protein.seq:
            if c == '-':
                seq += '---'
            else:
                seq += str(gene_seqs[my_id][pos:pos + 3])
                pos += 3
        al_genes.append(SeqRecord(Seq(seq), id=my_id))

    SeqIO.write(al_genes, '%s_align.fasta' % gene, 'fasta')
# -
