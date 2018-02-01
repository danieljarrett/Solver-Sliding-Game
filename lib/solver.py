from heap        import Heap
from collections import deque

class Solver(object):
    def __init__(self, initState, goalState):
        self.initState = initState
        self.goalState = goalState

        self.resetStats()

    ##################################################################
    # Breadth First Search
    ##################################################################

    def BFS(self):
        self.frontier = deque([self.initState])
        self.explored = set([self.initState])

        while self.frontier:
            state = self.frontier.popleft()

            if self.goalCheck(state):
                break

            self.expandBFS(state)

    def expandBFS(self, state):
        for state in state.neighbors():
            if state not in self.explored:
                self.frontier.append(state)
                self.explored.add(state)

                self.incrementTreeHeight(state)

        self.incrementExpanded()
        self.incrementMaxFringe()

    ##################################################################
    # Depth First Search
    ##################################################################

    def DFS(self):
        self.frontier = [self.initState]
        self.explored = set()

        while self.frontier:
            state = self.frontier.pop()

            if self.goalCheck(state):
                break

            self.expandDFS(state)

    def expandDFS(self, state):
        self.explored.add(state)

        for state in reversed(state.neighbors()):
            if state not in self.explored:
                self.frontier.append(state)

                self.incrementTreeHeight(state)

        self.incrementExpanded()
        self.incrementMaxFringe()

    ##################################################################
    # A* Search
    ##################################################################

    def AST(self):
        self.frontier = Heap([self.initState], self.priorityKey)
        self.explored = set()

        while not self.frontier.isEmpty():
            state = self.frontier.delete()

            if self.goalCheck(state):
                break

            self.expandAST(state)

    def expandAST(self, state):
        self.explored.add(state)

        for state in state.neighbors():
            if state not in self.explored:
                self.frontier.insert(state)

                self.incrementTreeHeight(state)

        self.incrementExpanded()
        self.incrementMaxFringe()

    def priorityKey(self, state):
        return state.fCost(self.goalState)

    ##################################################################
    # Heuristic DLS Iteration
    ##################################################################

    def DLS(self, cutoff):
        self.frontier = [self.initState]
        self.explored = set()

        while self.frontier:
            state = self.frontier.pop()

            if self.goalCheck(state):
                return True

            if state.fCost(self.goalState) >= cutoff:
                self.release(state)
                continue

            self.expandDLS(state)

    def expandDLS(self, state):
        neighbors = [neighbor for neighbor in state.neighbors() \
            if neighbor not in self.explored]

        if neighbors:
            self.explored.add(state)

            for index, neighbor in enumerate(reversed(neighbors)):
                neighbor.isLastChild = True if index == 0 else False
                self.frontier.append(neighbor)

                self.incrementTreeHeight(neighbor)
        else:
            self.release(state)

        self.incrementMaxFringe()
        self.incrementExpanded()

    def release(self, state):
        try:
            while state.isLastChild:
                state = state.priorState()
                self.explored.remove(state)
        except AttributeError:
            pass

    ##################################################################
    # IDA* Search
    ##################################################################

    def IDA(self):
        cutoff = self.initState.fCost(self.goalState)

        goalFound = False

        while not goalFound:
            goalFound = self.DLS(cutoff)

            cutoff += 2

    ##################################################################
    # Check Ror Goal State
    ##################################################################

    def goalCheck(self, state):
        if state == self.goalState:
            self.recordStats(state)

            return True

    ##################################################################
    # Increment Statistics
    ##################################################################

    def incrementExpanded(self):
        self.expanded += 1

    def incrementMaxFringe(self):
        if len(self.frontier) > self.maxFringe:
            self.maxFringe = len(self.frontier)

    def incrementTreeHeight(self, state):
        if state.gCost + 1 > self.treeHeight:
            self.treeHeight = state.gCost + 1

    ##################################################################
    # Output Statistics
    ##################################################################

    def printStats(self):
        for key in self.statistics:
            print key, self.statistics[key]

    def resetStats(self):
        self.expanded = 0
        self.maxFringe = 0
        self.treeHeight = 1

        self.statistics = {}

    def recordStats(self, state):
        path = []

        self.statistics['Cost of Path:     '] = state.gCost
        self.statistics['Nodes Expanded:   '] = self.expanded
        self.statistics['Fringe Size:      '] = len(self.frontier)
        self.statistics['Max Fringe Size:  '] = self.maxFringe
        self.statistics['Search Depth:     '] = state.gCost + 1
        self.statistics['Max Search Depth: '] = self.treeHeight

        while state.prior:
            path.insert(0, state.priorMove())

            state = state.priorState()

        if len(path) > 40:
            strPath = str(path[0:40]) + ' plus ' + \
                str(len(path) - 40) + ' more steps...'
        else:
            strPath = str(path)

        self.statistics['Path to Goal:     '] = strPath
