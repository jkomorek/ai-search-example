from sudoku_solver.engine.problem_solver import solve
from sudoku_solver.example1.simple_problem import SimpleProblem
from sudoku_solver.example1.simple_node import SimpleNode

def main():
    print("===== starting sudoku solver =====")

    problem = SimpleProblem()
    solution_node = solve(problem)


    print('\n====== Found solution ======')
    print(solution_node.as_solution())


if __name__ == "__main__":
    main()
