class Tile:
    def __init__(self, state):
        self.state = state

    def is_clean(self):
        return self.state == "0"

    def set_clean(self):
        self.state = 0


class Vacuum:
    def __init__(self, position):
        self.position = position
        self.tiles = []
        self.tiles_checked = []

    def add_tile(self, tile):
        self.tiles.append(tile)

    def turn_on(self):
        print("Vacuum started checking...")
        while not len(self.tiles_checked) == len(self.tiles):
            print(self.position, ", ", self.tiles[0].state, ", ", self.tiles[1].state)
            self.move()
        print(self.position, ", ", self.tiles[0].state, ", ", self.tiles[1].state)
        print("\nAll tiles clean")

    def move(self):

        if self.position == "A":
            self.check(self.tiles[0])
            if len(self.tiles_checked) != len(self.tiles):
                print("Moving vacuum to the right")
                self.position = "B"

        else:
            self.check(self.tiles[1])
            if len(self.tiles_checked) != len(self.tiles):
                print("Moving vacuum to the left")
                self.position = "A"

    def check(self, tile):
        if not tile.is_clean():
            print("Sucking Tile ", self.position)
            self.suck(tile)
        else:
            print("Tile ", self.position, " clean")
        if not self.tiles.index(tile) in self.tiles_checked:
            self.tiles_checked.append(self.tiles.index(tile))

    def suck(self, tile):
        tile.set_clean()


if __name__ == '__main__':
    """Inicio de la aplicación"""
    state = input("Enter state for room A: (0) for clean, (1) for dirty ")
    tile_a = Tile(state)
    state = input("Enter state for room B: (0) for clean, (1) for dirty ")
    tile_b = Tile(state)
    position = input("Enter initial position for vacuum (A or B):")
    vacuum = Vacuum(position)
    vacuum.add_tile(tile_a)
    vacuum.add_tile(tile_b)
    vacuum.turn_on()
