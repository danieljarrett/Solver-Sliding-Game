from board  import Board
from state  import State
from solver import Solver
from time   import time
from csv    import DictWriter

goalState = State(Board(range(9)))

methods = ['BFS', 'DFS', 'AST', 'IDA']

headers = False

##################################################################
# Single Iteration
##################################################################

def process(solver, method):
    solve = getattr(solver, method)

    t0 = time()

    solve()

    t1 = time()

    solver.statistics['Running Time:     '] = t1-t0
    solver.statistics['Search Method:    '] = method
    solver.statistics.pop('Path to Goal:     ', None)

##################################################################
# Output Iterations
##################################################################

with open('statistics.csv', 'wb') as f:
    for method in methods:
        for entropy in xrange(1, 1000, 1):
            initState = State(Board(range(9)))
            initState.board.scramble(entropy)

            solver = Solver(initState, goalState)

            process(solver, method)

            if not headers:
                w = DictWriter(f, solver.statistics.keys())
                w.writeheader()
                headers = True

            w.writerow(solver.statistics)
