
from sudoku_solver.engine.node import Node
from sudoku_solver.example1.simple_problem import Problem, SimpleProblem
from sudoku_solver.example1.simple_node import SimpleNode


def solve(problem: SimpleProblem):
    print("Solving problem")

    initial_state = problem.get_initial_state()

    # explored contains all nodes that have already been expanded. Checking new nodes against this prevents infinite loops.
    explored: [Node] = []
    
    # frontier contains all possible nodes (solutions). When empty there are no solultions.
    frontier = [initial_state]

    i = 0
    while (True):
        i = i+1
        print(f'iteration {i} with frontier', frontier)

        # if frontier is empty then no solution    
        if len(frontier) == 0:
            return None
        
        # remove node from the frontier
        node = frontier.pop()
        print(f'checking node [{node._state}]')

        # if node is goal, then return solution
        if problem.is_a_solution(node):
            print(f'solution!')
            return node
        print(f'not solution')

        # TODO:        
        # if node in explored:
        #     print(f)
        #     continue
    

        # expand node and add resulting nodes to frontier
        new_nodes = node.expand()
        print(f'expanded nodes: ', new_nodes)
        if new_nodes:
            frontier.extend(new_nodes)
