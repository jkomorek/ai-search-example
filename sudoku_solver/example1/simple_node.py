from sudoku_solver.engine.node import Node


class SimpleNode(Node):

    _parent = None
    _state = None

    def __init__(self, parent: Node, state) -> None:
        super().__init__()
        self._parent = parent
        self._state = state
        

    def as_solution(self):
        solution = []

        temp_node = self
        while(temp_node is not None):
            solution.append(temp_node)
            temp_node = temp_node._parent
        solution.reverse()
        return f'{solution}'
            

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



    def set_parent(self, parent: Node):
        self._parent = parent

    def __repr__(self):
        return f'{self._state}'

    def __str__(self):
        return f'{self._state}'
    
