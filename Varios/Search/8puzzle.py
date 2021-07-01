import numpy as np


class Puzzle():
    # Lista de los mejores nodes encontrados en cada nivel
    nodes = []
    cont = 0

    def __init__(self, initialState, finalState, heuristic):

        self.initialState = np.copy(initialState)
        self.finalState = np.copy(finalState)
        self.heuristic = heuristic

    # Funcion basada en las piezas mal colocadas
    def misplaced(self, actualState):

        valor = 0
        for i in range(len(actualState)):
            for j in range(len(actualState)):
                if actualState[i][j] != self.finalState[i][j] and actualState[i][j] != 0:
                    valor += 1
        return valor

    def manhattan(self, actualState):
        aux = 0
        for i in range(1, 9, 1):
            x1, y1 = self.getBlank(actualState, i)
            x2, y2 = self.getBlank(self.finalState, i)
            aux += abs(x1 - x2)
            aux += abs(y1 - y2)
        return aux

    def f(self, actualState):
        if self.heuristic == 1:
            return self.manhattan(actualState)
        return self.misplaced(actualState)

    def getBlank(self, puzzle, num):
        x = 0
        y = 0
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == num:
                    x = i
                    y = j
        return x, y

    def compare(self, actualState, finalState):
        # Compara dos estados del tablero#
        for i in range(len(actualState)):
            for j in range(len(actualState)):
                if actualState[i][j] != finalState[i][j]:
                    return False
        return True

    def check(self, puzzle):
        # Comprobar si no se repiten los nodos#
        for node in self.nodes:
            if self.compare(puzzle, node) == True \
                    and self.compare(puzzle, self.initialState) == False:
                return True
        return False

    def move(self, puzzle, x, y):

        auxPuzzle = np.copy(puzzle)
        node = np.copy(puzzle)
        # value maximo de la funcion
        value = 100

        # left
        if x - 1 >= 0:
            aux = puzzle[x][y]
            puzzle[x][y] = puzzle[x - 1][y]
            puzzle[x - 1][y] = aux
            value1 = self.f(puzzle)
            if value1 < value and self.check(puzzle) == False:
                node = np.copy(puzzle)
                value = value1

        puzzle = np.copy(auxPuzzle)

        # right
        if x + 1 <= 2:
            aux = puzzle[x][y]
            puzzle[x][y] = puzzle[x + 1][y]
            puzzle[x + 1][y] = aux
            value1 = self.f(puzzle)
            if value1 <= value and self.check(puzzle) == False:
                node = np.copy(puzzle)
                value = value1

        puzzle = np.copy(auxPuzzle)

        # down
        if y - 1 >= 0:
            aux = puzzle[x][y]
            puzzle[x][y] = puzzle[x][y - 1]
            puzzle[x][y - 1] = aux
            value1 = self.f(puzzle)
            if value1 < value and self.check(puzzle) == False:
                node = np.copy(puzzle)
                value = value1

        puzzle = np.copy(auxPuzzle)

        # up
        if y + 1 <= 2:
            aux = puzzle[x][y]
            puzzle[x][y] = puzzle[x][y + 1]
            puzzle[x][y + 1] = aux
            value1 = self.f(puzzle)
            if value1 < value and self.check(puzzle) == False:
                node = np.copy(puzzle)
                value = value1

        self.nodes.append(node)  # El mejor nodo se agrega a la lista de nodos

        print("\n", node)
        print("N=", self.f(node))

        return node

    def getNode(self, actual):
        print("Paso: ", self.cont)
        self.cont += 1
        # Crea un node a partir del nodo anterior siempre y cuando no sea el nodo con el estado final#
        x, y = self.getBlank(actual, 0)  # Se busca la posición 0 para determinar el siguiente movimiento
        actual = np.copy(self.move(actual, x, y))
        if not self.compare(actual, self.finalState):
            return self.getNode(actual)  # LLamado recursivo con la nueva matriz resultante


    def solve(self):
        # Función principal a la que llamara el programa al iniciar
        actualState = np.copy(self.initialState)
        print(self.initialState, "\n N=", self.f(self.initialState))
        self.getNode(actualState)


# funcion que ejecutará el inicio del programa#
A = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
B = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
heuristica = 1
if heuristica == 1:
    funcion = "Numero de piezas mal ubicadas"
else:
    funcion = "Suma de las distancias"
print("N=", funcion)
p = Puzzle(A, B, heuristica)
p.solve()
