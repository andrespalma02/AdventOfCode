# se declara la clase aspiradora
class Vacuum:

    def __init__(self, initial_state):
        # Tabla de estados
        # 1 significa sucio
        # 0 significa limpio
        self.states = [
            (1, 1, 1, "A"), (1, 1, 1, "B"), (1, 1, 1, "C"),  # 0, 1, 2,
            (1, 1, 0, "A"), (1, 1, 0, "B"), (1, 1, 0, "C"),  # 3, 4, 5
            (1, 0, 1, "A"), (1, 0, 1, "B"), (1, 0, 1, "C"),  # 6, 7, 8
            (1, 0, 0, "A"), (1, 0, 0, "B"), (1, 0, 0, "C"),  # 9, 10,11
            (0, 1, 1, "A"), (0, 1, 1, "B"), (0, 1, 1, "C"),  # 12,13,14
            (0, 1, 0, "A"), (0, 1, 0, "B"), (0, 1, 0, "C"),  # 15,16,17
            (0, 0, 1, "A"), (0, 0, 1, "B"), (0, 0, 1, "C"),  # 18,19,20
            (0, 0, 0, "A"), (0, 0, 0, "B"), (0, 0, 0, "C")  # 21, 22,23
        ]

        self.actual_state = initial_state
        self.iterations = 1

    # mientras no se alcance el estado objetivo la aspiradora sigue inspeccionando el espacio
    def turn_on(self):
        while self.actual_state != self.states[21] \
                and self.actual_state != self.states[22] \
                and self.actual_state != self.states[23]:
            print("State ", self.states.index(self.actual_state), ": ", self.actual_state)
            self.check()
        print("State ", self.states.index(self.actual_state), ": ", self.actual_state)
        print("All rooms are clean!!")
        print(self.iterations, " iterations needed")

    # el metodo check se encarga de realizar transciones entre los estados de acuerdo a la tabla
    def check(self):
        index = self.states.index(self.actual_state)
        '''
        Hay transiciones que cumplen ciertos patrones, por lo que se optimizo el codigo aplicando
        los patrones encontrados
        '''
        if index == 0 or index == 3 or index == 6 or index == 9:
            print("suck")
            self.actual_state = self.states[index + 12]

        elif index == 1 or index == 4 or index == 13 or index == 16:
            print("suck")
            self.actual_state = self.states[index + 6]

        elif index == 2 or index == 8 or index == 14 or index == 20:
            print("suck")
            self.actual_state = self.states[index + 3]

        elif index == 5 or index == 7 or index == 10 or index == 11 or index == 17:
            print("left")
            self.actual_state = self.states[index - 1]

        elif index == 12 or index == 15 or index == 18 or index == 19:
            print("right")
            self.actual_state = self.states[index + 1]

        # el costo se mide por las iteraciones necesarias para llegar al estado objtetivo
        self.iterations += 1


state_a = input("Enter state for room A: (0) for clean, (1) for dirty ")
state_b = input("Enter state for room B: (0) for clean, (1) for dirty ")
state_c = input("Enter state for room C: (0) for clean, (1) for dirty ")
position = input("Enter initial position for vacuum (A, B, C):")
vacuum = Vacuum((int(state_a), int(state_b), int(state_c), position))
vacuum.turn_on()
