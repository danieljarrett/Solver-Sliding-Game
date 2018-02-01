State Space Search
====

A Comparative Analysis of Methodologies in State Space Search for the Sliding Tile n-Puzzle.

### Overview

A sliding-tile puzzle consists of a board holding distinct movable tiles, and an empty space. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. Given an initial board and a goal board, the combinatorial search problem is to find a sequence of moves that transitions the former to the latter. The search space is the set of all possible boards reachable from the initial board.

In terms of knowledge representation, we model the problem formulation with object-oriented principles of modularity and encapsulation. An instance of a board is represented by a Board object (see board.py). Each board is uniquely and completely identified by the configuration of tiles on the board, represented internally by an array of integer tiles. We represent a search node with a State object (see state.py). Each state consists of an internal board instance, the cumulative scalar path cost incurred to reach the board, and a reference to the prior state.

The implicit graph of the combinatorial search problem is fully specified by the state space, i.e. the set of all possible states reachable from the initial state, and the transition model, i.e. the set of all legal moves that allow transitioning between states. We implement a search instance for the implicit graph with an explicit tree, the structure of which is generated dynamically by a method in a Solver object (see solver.py). 

### Solve A Game Board

 To solve a given board, navigate to the code directory, and type:


      "python driver.py METHOD BOARD"


  `METHOD`` can be one of the following:


      * "bfs" -- Breadth First Search

      * "dfs" -- Depth First Search

      * "ast" -- A Star Search

      * "ida" -- IDA Star Search


  `BOARD` must be a comma-separated list of integers, with no spaces. For example:


      "python driver.py bfs 0,8,7,6,5,4,3,2,1"




  To solve a random board, navigate to the code directory, and type:


      "python driver.py METHOD DIMENSION"


  `DIMENSION` must be a single integer. For example:


      "python driver.py bfs 3"

### Bulk Test Statistics

While the above examples anecdotally verify theoretical complexities, they are not sufficient for illustrative purposes. Therefore we have developed and run each of the four search algorithms on a set of 999 randomly scrambled legal boards, with entropy levels ranging from one to 1,000 in increments of one, where entropy is defined as the number of scrambling moves applied.

Exhibits 1–4 illustrate the time and space complexities associated with each of the four search algorithms. In Exhibit 1, we see more clearly that the time and space complexities of BFS are exponential in the depth of the solution. In particular, note the aforementioned explored-set effect illustrated by the leveling-off of the exponential growths when the cost-of-path increases past some point around 22 moves—as we approach the maximum depth of the search tree, the possibilities quickly narrow down, and many branches rapidly result in dead ends.

In Exhibit 2, we see more clearly that the space complexity of DFS is generally linear in the maximum height of the tree. Observe that the time complexity also seems much more linear than the exponential bound would suggest. Again, this is due to the the nature of the sliding-tile state space: DFS seldom hits dead-ends until it almost exhausts the possibilities of board permutations. In other words, it rarely backtracks, and for the most part makes a beeline downwards. The exponential nature dominates only at very high cost paths above 100,000.

Exhibits 3 and 4 illustrate similar properties of the heuristic algorithms. Note that both dimensions of complexity are much improved over their non-heuristic counterparts. Due to the lower rates of expansion, the respective exponential and linear growth orders are much more apparent. Finally, Exhibits 5–8 illustrate the linear relationship between the running time and the number of nodes expanded, justifying the claims to linear proxy made earlier.

### Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request