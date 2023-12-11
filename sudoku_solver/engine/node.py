from abc import ABC, abstractmethod

class Node(ABC):

    # Represents this current state of the node allowing future states to be dervied from actions
    _state = None

    # Return all possible nodes that could be next.
    @abstractmethod
    def expand():
        pass


    # SHould return true if two nodes contain an equivelent state, meaning that they represent the same node in a graph
    def __eq__(self, __value: object) -> bool:

        #TODO: check to see if provided object is even a Node
        return self._state.__eq__(__value._state)