
from abc import ABC
from sudoku_solver.engine.node import Node
from sudoku_solver.example1.simple_node import SimpleNode


class Problem(ABC):
    pass


class SimpleProblem(Problem):

    # creates a Node representing the initial state of the problem to be solved.
    def get_initial_state(self) -> Node:
        return SimpleNode(parent=None, state=0)

    # returns true if the supplied node represents a solution to the problem
    def is_a_solution(self, node: SimpleNode):
        return node._state == 10
    

    def expand(self):
        tree = {
            0: [1, 2],
            1: [3, 4],
            2: [5, 6],
            3: [7, 8],
            4: [9, 10]
        }

        children = tree.get(self._state)        
        if children:
            return list(map(lambda x: SimpleNode(self, x), children))


