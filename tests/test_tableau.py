# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:42:14 2019

@author: tschu
"""
import sys
sys.path.insert(1, '../src')

import tableau
import unittest
import numpy as np

class TestTableauCreation(unittest.TestCase):
    """ Test creating a simplex tableau """
    
    def setup_data(self, ):
        """ Simple function for providing test data """
        A = [[1, 1, -1, 0, 0, 1, 0],
             [2, -1, 0, -1, 0, 0, 1],
             [0, 3, 0, 0, 1, 0, 0]]
        b = [1, 1, 2]
        c = [3, 0, -1, -1, 0, 0, 0, 2]

        return A, b, c
    
    
    def test_creating_minimization_problem(self, ):
        A, b, c = self.setup_data()
        tab = tableau.Tableau()
        tab.add_objective(c, False)
        
        self.assertEqual(c, tab.tab.tolist()[-1])
    
    
    def test_creating_maximization_problem(self, ):
        A, b, c = self.setup_data()
        tab = tableau.Tableau()
        tab.add_objective(c, True)
        
        self.assertEqual([-entry for entry in c], tab.tab.tolist()[-1])
    
    
    def test_adding_constraints(self, ):
        A, b, c = self.setup_data()
        tab = tableau.Tableau()
        tab.add_constraints(A, b)
        
        constraints = self.create_constraints_as_list(A, b)
        
        self.assertEqual(tab.tab.tolist(), constraints)
    
    
    def test_adding_constraints_before_adding_objective(self, ):
        A, b, c = self.setup_data()
        tab = tableau.Tableau()
        tab.add_constraints(A, b)
        tab.add_objective(c, False)
        
        constraints = self.create_constraints_as_list(A, b)
        constraints.append(c)
        
        self.assertEqual(tab.tab.tolist(), constraints)
    
    
    def test_adding_constraints_after_adding_objective(self, ):
        A, b, c = self.setup_data()
        tab = tableau.Tableau()
        tab.add_objective(c, False)
        tab.add_constraints(A, b)
        
        constraints = self.create_constraints_as_list(A, b)
        constraints.append(c)
        
        self.assertEqual(tab.tab.tolist(), constraints)
    
    
    def create_constraints_as_list(self, A, b):
        """ 
        Abbreviation for test funtions to create a list of lists that
        represents the set of constraints
        """
        
        A_transpose = np.transpose(A).tolist()
        A_transpose.append(b)
        return np.transpose(A_transpose).tolist()
        

if __name__ == '__main__':
    unittest.main()