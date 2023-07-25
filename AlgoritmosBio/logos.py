from Bio import SeqIO
from Bio.SeqLogo import SeqLogo
import matplotlib.pyplot as plt

# Read the input sequences from a FASTA file
sequences = []
for record in SeqIO.parse("input.fasta", "fasta"):
    sequences.append(record.seq)

# Create a sequence alignment object
alignment = SeqIO.AlignIO.MultipleSeqAlignment(sequences)

# Create a sequence logo object
seqlogo = SeqLogo(alignment)

# Set the figure size and style
plt.figure(figsize=(8, 4))
plt.style.use('seaborn-whitegrid')

# Plot the sequence logo
seqlogo.plot(ax=plt.gca())

# Set the axis labels and title
plt.xlabel("Position")
plt.ylabel("Information content (bits)")
plt.title("Sequence logo")

# Show the plot
plt.show()