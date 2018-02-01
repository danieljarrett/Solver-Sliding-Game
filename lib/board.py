from math   import sqrt
from array  import array
from random import choice
from copy   import copy

class Board(object):
    def __init__(self, tiles):
        if not self.checkTiles(tiles):
            raise ValueError("Input tiles invalid")

        self.tiles = array('I', tiles)
        self.space = tiles.index(0)
        self.width = int(sqrt(len(tiles)))

    ##################################################################
    # Tile Mover
    ##################################################################

    def move(self, direction):
        self.tiles[self.space] = self.tiles[direction]
        self.tiles[direction] = 0
        self.space = direction

    ##################################################################
    # Directions
    ##################################################################

    def up(self):
        if self.space / self.width == 0:
            raise IndexError("Tile out of bounds")

        return self.space - self.width

    def down(self):
        if self.space / self.width == self.width - 1:
            raise IndexError("Tile out of bounds")

        return self.space + self.width

    def left(self):
        if self.space % self.width == 0:
            raise IndexError("Tile out of bounds")

        return self.space - 1

    def right(self):
        if self.space % self.width == self.width - 1:
            raise IndexError("Tile out of bounds")

        return self.space + 1

    ##################################################################
    # Scramble Board
    ##################################################################

    def scramble(self, times):
        for time in xrange(times):
            try:
                self.move(choice(self.directions())())
            except IndexError:
                pass

    def directions(self):
        return [self.up, self.down, self.left, self.right]

    ##################################################################
    # Distance Functions
    ##################################################################

    def hammingDistance(self, other):
        counter = 0

        for index, tile in enumerate(self.tiles):
            if tile != 0 and tile != other.tiles[index]:
                counter += 1

        return counter

    def manhattanDistance(self, other):
        counter = 0

        for index, tile in enumerate(self.tiles):
            if tile != 0 and tile != other.tiles[index]:
                currY, currX = divmod(index, self.width)
                goalY, goalX = divmod(other.tiles.index(tile), self.width)

                distance = abs(goalX - currX) + abs(goalY - currY)
                counter += distance

        return counter

    ##################################################################
    # Check Input Tiles
    ##################################################################

    def checkTiles(self, tiles):
        check = copy(tiles)
        check.sort()

        isProper = check == range(len(tiles))
        isSquare = sqrt(len(tiles)) == int(sqrt(len(tiles)))

        return isProper and isSquare

    ##################################################################
    # Method Overrides
    ##################################################################

    def __eq__(self, other):
        if other is self:
            return True

        if other is None:
            return False

        if not isinstance(other, Board):
            return False

        return self.tiles == other.tiles

    def __hash__(self):
        return hash(self.tiles.tostring())

    def __str__(self):
        divider = '-' * (8 * self.width + 1) + '\n'
        padding = '|       ' * self.width + '|\n'

        result = divider

        for i in range(self.width):
            result += padding + '|'

            for j in range(self.width):
                tile = self.tiles[i * self.width + j]
                result += ('    ' if tile == 0 else "%4d"%tile) + '   |'

            result += '\n' + padding + divider

        return result
