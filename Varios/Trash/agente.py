class Vacuum():
    def __init__(self, status, location):
        self.position_table = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        self.status = status
        self.location = self.position_table[location]
        self.action = None
        self.iterations = 1

    def turn_on(self):

        while self.status != [0, 0, 0]:
            keys = [k for k, v in self.position_table.items() if v == self.location]
            print(self.status, ", ", keys)
            self.check()
        print(self.status, ", ", keys)
        print("All rooms are clean!!")

    def check(self):
        if self.status[self.location] == 1:
            self.status[self.location] = 0
            print("suck")
        elif self.location == 0:
            self.location += 1
            self.action = "right"
            print("right")
        elif self.location > 0 and len(self.status) - 1:
            if self.action == "right":
                self.location += 1
                self.action = "right"
                print("right")
            else:
                self.location -= 1
                self.action = "left"
                print("left")

        elif self.location == len(self.status) - 1:
            self.location -= 1
            self.action = "left"
            print("left")


state_a = int(input("Enter state for room A: (0) for clean, (1) for dirty "))
state_b = int(input("Enter state for room B: (0) for clean, (1) for dirty "))
state_c = int(input("Enter state for room C: (0) for clean, (1) for dirty "))
position = input("Enter initial position for vacuum (A, B, C:")
status = [state_a, state_b, state_c]
vacuum = Vacuum(status, position)
vacuum.turn_on()
