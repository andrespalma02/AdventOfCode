import re

from Bio import Entrez

# Especifica tu dirección de correo electrónico para que Entrez pueda contactarte en caso de problemas
Entrez.email = "tucorreo@example.com"



def process(file):
    regex = r"N[^P][S|T][^P]"
    for line in file:
        print(line.split("_")[0])

        # Especifica el término de búsqueda utilizando el identificador de la proteína
        search_term = line.split("_")[0] if line.split("_")[0] else ""

        # Realiza la búsqueda utilizando esearch
        search_handle = Entrez.esearch(db="protein", term=search_term)

        # Lee los resultados de la búsqueda en un objeto de tipo Record
        search_record = Entrez.read(search_handle)

        # Cierra la conexión con Entrez
        search_handle.close()
        id_list = search_record["IdList"]
        # Especifica el tipo de información que deseas obtener (por ejemplo, fasta)
        retrieve_type = "fasta"

        # Realiza la recuperación utilizando efetch
        retrieve_handle = Entrez.efetch(db="protein", id=id_list[0], rettype=retrieve_type, retmode="text")

        # Lee la información obtenida en un objeto de tipo string
        retrieve_data = retrieve_handle.read()

        # Cierra la conexión con Entrez
        retrieve_handle.close()

        # Imprime la información obtenida
        #print(retrieve_data)

        matches = re.finditer(r"N[^P][S|T][^P]", retrieve_data)
        for match in matches:
            print(match.start() + 1, end=" ")


with open("rosalind_mprt.txt") as file:
    protein = file.readlines()
    print(process(protein))