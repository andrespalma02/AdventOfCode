f = open("input.txt")

# Guardamos cada línea como un elemento de una lista
lines = f.readlines()
lines = [line.rstrip() for line in lines]


# Primera Parte
def primera_parte(lines):
    contador_global = 0
    linea_visitada = set()
    contador_por_linea = 0
    solucion_valida = True
    while True:
        # Suponiendo que recorrimos todas las líneas y no se encontraron bucles
        if len(lines) - 1 == contador_por_linea:
            solucion_valida = False

        # Solucion de la primera parte para eliminar los bucles
        if contador_por_linea in linea_visitada:  # iteramos por cada línea visitada
            solucion_valida = False  # buscando una solucion válida a cada una de las instrucciones
            return contador_global, solucion_valida

        inst, contador = lines[contador_por_linea].split(" ")
        contador = int(contador)
        linea_visitada.add(contador_por_linea)
        # si encuentra una operacion nop el contador por línea aumenta en 1 para que lea
        # la siguiente instrcuccion sin hacer nada
        if inst == "nop":
            contador_por_linea += 1
        # si encuentra una operacion acc el contador aumenta tantas veces como
        # esta definida en la operacion acc y lee la siguiente linea
        if inst == "acc":
            contador_global += contador
            contador_por_linea += 1
        # si encuentra una operacion jump el contador por línea aumenta tantas veces como esta
        # definida en la operacion jmp y empieza a leer la línea definida por jmp
        if inst == "jmp":
            contador_por_linea += contador

        # Cuando ya se ha encontrado la solucion valida entonces retornamos el contador global
        if solucion_valida == False:
            return contador_global, True


print("Contador primera parte: ", primera_parte(lines)[0])


# Segunda Parte
def segunda_parte(lines):
    contador_actual = 0
    linea_visitada = []
    linea_actual = 0
    lineas_nuevas = lines.copy()
    # recorremos la lista por cada una de las líneas nuevas
    for linea_actual in range(1, len(lineas_nuevas)):
        inst, contador_global = lines[linea_actual].split(" ")
        contador_global = int(contador_global)  # definimos un contador global

        # Aqui cambiamos la instruccion nop por una instruccion jmp y viceversa hasta que ya no exista un bucle infinito
        if inst == "nop":
            inst = "jmp"
        elif inst == "jmp":
            inst = "nop"

        linea_visitada = []
        lineas_nuevas = lines.copy()
        # Aqui asignamos el nuevo valor a la instruccion nop o jmp
        lineas_nuevas[linea_actual] = " ".join((inst, str(contador_global)))
        contador_global, valid = primera_parte(lineas_nuevas)
        # Si se ha tenido exito y se ha salido del bucle infinito retornaremos el contador global
        if valid:
            return contador_global


print("Contador segunda parte: ", segunda_parte(lines))
