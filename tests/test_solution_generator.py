import pytest

from solver import NeedlemanWunshSolver
from solution_generator import SolutionGenerator

def test_generate_max_n_solutions():
    solver = NeedlemanWunshSolver(5, -5, -2)
    a = 'SAM'
    b = 'SUM'
    _, directions, _ = solver.solve(a, b)
    max_solutions = 1
    solutions = [x for x in SolutionGenerator(directions, a, b, max_solutions)]
    assert(len(solutions) == max_solutions)

def test_generate_all_solutions_1():
    solver = NeedlemanWunshSolver(5, -5, -2)
    a = 'BUM'
    b = 'SUM'
    _, directions, _ = solver.solve(a, b)
    max_solutions = 15
    solutions = [x for x in SolutionGenerator(directions, a, b, max_solutions)]
    assert solutions[0].a == '_BUM'
    assert solutions[0].b == 'S_UM'
    assert solutions[1].a == 'B_UM'
    assert solutions[1].b == '_SUM'

def test_generate_all_solutions_2():
    solver = NeedlemanWunshSolver(5, -5, -2)
    a = 'SUM'
    b = 'SUL'
    _, directions, _ = solver.solve(a, b)
    max_solutions = 15
    solutions = [x for x in SolutionGenerator(directions, a, b, max_solutions)]
    assert solutions[0].a == 'SU_M'
    assert solutions[0].b == 'SUL_'
    assert solutions[1].a == 'SUM_'
    assert solutions[1].b == 'SU_L'

def test_generate_all_solutions_3():
    solver = NeedlemanWunshSolver(5, -5, -2)
    a = 'SUM'
    b = 'SAM'
    _, directions, _ = solver.solve(a, b)
    max_solutions = 15
    solutions = [x for x in SolutionGenerator(directions, a, b, max_solutions)]
    assert solutions[0].a == 'S_UM'
    assert solutions[0].b == 'SA_M'
    assert solutions[1].a == 'SU_M'
    assert solutions[1].b == 'S_AM'
