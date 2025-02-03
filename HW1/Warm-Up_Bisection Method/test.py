import numpy as np
import bisection_method as bm
import math
import example_functions as ef


def test_bs_method():
    solver = bm.BisectionSolver()

    a =
    b =
    known_answer = 1.5
    assert np.isclose( solver.solve( ef.func_example1, a, b ) , known_answer)

    a = 1
    b = 4
    known_answer = 2
    assert np.isclose( solver.solve( ef.func_example2, a, b ) , known_answer)


    a = -7.5
    b = 5
    known_answer = -7
    assert np.isclose( solver.solve( ef.func_example3, a, b ) , known_answer)


    a = 0
    b = 5 * np.pi / 4
    known_answer = np.pi/2
    assert np.isclose( solver.solve( ef.func_example4, a, b ) , known_answer)

    a = 0
    b = 1
    known_answer = 0.443568
    assert np.isclose( solver.solve( ef.func_example5, a, b ) , known_answer)

    a = -1
    b = 0
    known_answer = -0.703467
    assert np.isclose( solver.solve( ef.func_example6, a, b ) , known_answer)


    a = 0.001
    b = np.pi / 4 - 0.001
    known_answer = 0.6877752322144834
    assert np.isclose( solver.solve( ef.func_example7, a, b ) , known_answer)

    a = 0.001
    b = 10
    known_answer = 8.82798576742547
    assert np.isclose( solver.solve( ef.func_example8, a, b ) , known_answer)