from copy import deepcopy

class State(object):
    def __init__(self, board, prior = None, gCost = 0):
        self.board = board
        self.prior = prior
        self.gCost = gCost

    ##################################################################
    # Adjacent Nodes
    ##################################################################

    def neighbors(self):
        states = map(self.permute, self.board.directions())

        return [state for state in states if state is not None]

    ##################################################################
    # Neighbor Helper
    ##################################################################

    def permute(self, direction):
        try:
            direction()

            board = deepcopy(self.board)
            board.move(direction())

            prior = (self, direction.__name__.capitalize())
            gCost = self.gCost + 1

            return State(board, prior, gCost)
        except IndexError:
            pass

    ##################################################################
    # Prior Accessors
    ##################################################################

    def hasPrior(self):
        return True if self.prior else False

    def priorState(self):
        return self.prior[0] if self.hasPrior() else None

    def priorMove(self):
        return self.prior[1] if self.hasPrior() else None

    ##################################################################
    # Cost Functions
    ##################################################################

    def fCost(self, other):
        return self.gCost + self.hCost(other)

    def hCost(self, other):
        # return self.hammingPriority(other)
        return self.manhattanPriority(other)

    ##################################################################
    # Priority Functions
    ##################################################################

    def hammingPriority(self, other):
        return self.board.hammingDistance(other.board)

    def manhattanPriority(self, other):
        return self.board.manhattanDistance(other.board)

    ##################################################################
    # Method Overrides
    ##################################################################

    def __eq__(self, other):
        if other is self:
            return True

        if other is None:
            return False

        if not isinstance(other, State):
            return False

        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __str__(self):
        return self.board.__str__()
