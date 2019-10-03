# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:48:41 2019

@author: tschu
"""

import simplex
import unittest

class TestSimplex(unittest.TestCase):
    """ Tests for solving a simplex tableau """
    
    def setup_model(self, ):
        """ Simple function for providing test data """
        A = [[1, 1, -1, 0, 0, 1, 0],
             [2, -1, 0, -1, 0, 0, 1],
             [0, 3, 0, 0, 1, 0, 0]]
        b = [1, 1, 2]
        c = [3, 0, -1, -1, 0, 0, 0, 2]
        
        model = simplex.Simplex()
        model.add_constraints(A, b)
        model.add_objective(c, False)
        
        return model

    def test_finding_pivot_element(self, ):
        model = self.setup_model()
        
        model._calculate_pivot_position()
        
        self.assertEqual(model.pivot_column, 0)
        self.assertEqual(model.pivot_row, 1)


    def test_single_simplex_iteration(self, ):
        model = self.setup_model()
        
        model._calculate_pivot_position()
        model._perform_simplex_step()
        
        expected_solution = [[0, 1.5, -1, 0.5, 0, 1, -0.5, 0.5],
                             [1, -0.5, 0, -0.5, 0, 0, 0.5, 0.5],
                             [0, 3, 0, 0, 1, 0, 0, 2],
                             [0, 1.5, -1, 0.5, 0, 0, -1.5, 0.5]]
        
        self.assertEqual(model.tab.tolist(), expected_solution)
    
    
    def test_multiple_simplex_iterations(self, ):
        model = self.setup_model()
        solution = model.solve()
        
        expected_tableau = [[0, 3, -2, 1, 0, 2, -1, 1],
                            [1, 1, -1, 0, 0, 1, 0, 1],
                            [0, 3, 0, 0, 1, 0, 0, 2],
                            [0, 0, 0, 0, 0, -1, -1, 0]]
        expected_solution = [1, 0, 0, 1, 2, 0, 0]
        
        self.assertEqual(model.tab.tolist(), expected_tableau)
        self.assertEqual(solution.tolist(), expected_solution)

if __name__ == '__main__':
    unittest.main()