from Bio.Seq import Seq
f=open("rosalind_ini.txt","r")
my_seq = Seq(f.readline())
print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))
