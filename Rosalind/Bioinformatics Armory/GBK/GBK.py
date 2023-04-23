from Bio import Entrez

Entrez.email = "your_name@your_mail_server.com"


def count_entries(genus, start_date, end_date):
    # crear la consulta
    query = f"{genus}[Organism] AND ({start_date}[Publication Date] : {end_date}[Publication Date])"

    # buscar
    handle = Entrez.esearch(db="nucleotide", term=query)
    record = Entrez.read(handle)

    print(record['Count'])


f = open("rosalind_gbk.txt", "r")

genus = f.readline().strip()
start_date = f.readline().strip()
end_date = f.readline().strip()
count_entries(genus, start_date, end_date)
