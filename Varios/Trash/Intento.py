# Resolver el problema de los genes
# Solución
# Nombres: Isabel Balboa y Nicole Oleas
print("Pontificia Universidad Católica del Ecuador")


def usuario():
    nombre = input("Ingrese su nombre: ")
    return nombre


def Saludar(nombre):
    print("Buenos días ")


n = usuario()
Saludar(n)

# ("En este programa se utilizará un genes txt. para la resolución del problema de los genes")
# ("contenido: variable que almacena el contenido del archivo 'genes.txt' después de leerlo.")
# ("case: variable que lleva el control del número de caso que se está procesando.")
# ("#n: variable que indica el tamaño del genoma.")
# ("genome: lista que representa el genoma.")
# ("#r: variable que indica la cantidad de mutaciones reversas que se van a aplicar al genoma.")
# ("q: variable que indica la cantidad de consultas que se van a hacer al genoma.")


# Apertura del archivo con el que se va a proceder a trabajar
with open("genes.txt", "r") as archivo:
    contenido = archivo.read()


# Aplicar las mutaciones reversas
def mutación_reversa(genome, i,
                     j):  # mutación_reversa: función que realiza la mutación reversa en un genoma dado los índices i y j.
    # Aplica la mutación reversa (i, j) al genoma.
    genome[i - 1:j] = reversed(genome[i - 1:j])


def mutaciones(genome, mutations):  # mutaciones: función que aplica una lista de mutaciones reversas a un genoma.
    # Simula las mutaciones reversas en el genoma.
    for i, j in mutations:
        mutación_reversa(genome, i, j)


def posición(genome, gene):  # posición: función que busca la posición de un gen en un genoma.
    # Busca la posición del gen en el genoma.
    return genome.index(gene) + 1


# Lectura de datos desde el archivo genes.txt para poder realizar los ejercicios
with open('genes.txt', 'r') as f:  # Permite la lectura de los datos de los ejercicios
    case = 1
    while True:
        n = int(f.readline().strip())
        if n == 0:
            break
        genome = list(range(1, n + 1))
        r = int(f.readline().strip())
        mutations = [tuple(map(int, f.readline().strip().split())) for _ in range(r)]
        q = int(f.readline().strip())
        queries = [int(f.readline().strip()) for _ in range(q)]

        # Mutaciones reversas
        mutaciones(genome, mutations)

        # Consultas 
        print(f'Genoma {case}')
        with open('out.txt', 'a') as out_file:
            out_file.write(f'Genoma {case}\n')
            for query in queries:
                position = posición(genome, query)
                print(position)
                out_file.write(f'{position}\n')

        case += 1

print("Gracias por realizar el ejercicio")
