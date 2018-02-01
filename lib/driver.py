import resource

from board  import Board
from state  import State
from solver import Solver
from time   import time
from sys    import argv

##################################################################
# Get Initial Board
##################################################################

try:
    if ',' in argv[2]:
        tiles = argv[2].split(',')
        length = len(tiles)

        initBoard = Board(map(lambda tile: int(tile), tiles))

    else:
        length = int(argv[2]) ** 2

        initBoard = Board(range(length))
        initBoard.scramble(1000)

##################################################################
# Get Search Method
##################################################################

    method = argv[1].upper()

except (IndexError, ValueError):
    print '\nINSTRUCTIONS: Please enter:\n'
    print '(1) the Search Method as the first argument, and'
    print '(2) the Starting Board as the second argument, ' + \
            'formatted with no spaces like 2,3,1,5,8,9,7,6,0\n'
    print 'NOTE: To generate a completely random board of ' + \
          'width N, simply provide the value of N as the ' + \
          'second argument\n'

    exit()

##################################################################
# Define Problem
##################################################################

initState = State(initBoard)
goalState = State(Board(range(length)))

print initState

##################################################################
# Search For Solution
##################################################################

solver = Solver(initState, goalState)
solve = getattr(solver, method)

m0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1.0 / (1024 ** 2)
t0 = time()

solve()

t1 = time()
m1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1.0 / (1024 ** 2)

solver.printStats()

print 'Running Time:      ' + str(t1 - t0) + ' seconds'
print 'Max RAM Usage:     ' + str(m1 - m0) + ' MB'
