import pytest
import numpy as np

from solver import NeedlemanWunshSolver
from directions import Directions

def test_score_matrix_creation():
    solver = NeedlemanWunshSolver(2,-3,-2)
    score_mat = solver._get_score_matrix((3,3))
    assert score_mat.shape == (3,3)
    expected = np.array([[0, -2, -4],
                        [-2, 0, 0],
                        [-4, 0, 0]])
    assert (score_mat == expected).all()

def test_score_calculation():
    solver = NeedlemanWunshSolver(5, -5, -2)
    score_mat, _, final_score = solver.solve('SAM', 'SUM')
    expected = np.array([[ 0, -2, -4, -6],
                        [-2,  5,  3,  1],
                        [-4,  3,  1, -1],
                        [-6,  1, -1,  6]])
    assert (score_mat == expected).all()
    assert 6.0 == final_score

def test_final_score_extraction():
    score_mat = np.array([[ 0, -2, -4, -6],
                        [-2,  5,  3,  1],
                        [-4,  3,  1, -1],
                        [-6,  1, -1,  6]])
    assert NeedlemanWunshSolver._get_final_score_from_score_mat(score_mat) == 6.0

def test_directions_when_same():
    solver = NeedlemanWunshSolver(5, -5, -2)
    _, directions, _  = solver.solve('S', 'S')
    expected = Directions((2,2))
    expected.set_directions(1,1, diag=True)
    assert (directions.directions == expected.directions).all()

def test_directions_when_different():
    solver = NeedlemanWunshSolver(5, -5, -2)
    _, directions, _  = solver.solve('S', 'A')
    expected = Directions((2,2))
    expected.set_directions(1,1, left=True, up=True)
    assert (directions.directions == expected.directions).all()
    



