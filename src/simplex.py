# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:45:19 2019

@author: tschu
"""

import numpy as np
from tableau import Tableau

class Simplex(Tableau):
    """ Simplex method for tableaus containing a basic feasible solution """
    
    
    def __init__(self, ):
        super().__init__()
        
        self.pivot_column = 0
        self.pivot_row = 0
    
    
    def solve(self, ):
        """ 
        Solve the given model using standard simplex method
        
        Returns
        -------
        x : 1-d array of floats
            Solution array
        """
        while np.max(self.tab[-1,:-1]) > 0:
            self._calculate_pivot_position()
            self._perform_simplex_step()
        
        return self._read_solution()
            
    
    def _calculate_pivot_position(self, ):
        obj_coeffs = 1.0 * self.tab[-1, :-1]
        obj_coeffs[obj_coeffs <= 0] = np.inf
        self.pivot_column = np.argmin(obj_coeffs)
            
        with np.errstate(divide='ignore'):
            rhs_over_lhs = self.tab[:-1, -1] / self.tab[:-1, self.pivot_column]
        rhs_over_lhs[rhs_over_lhs <= 0] = np.inf
        rhs_over_lhs[np.isnan(rhs_over_lhs)] = np.inf
        
        self.pivot_row = np.argmin(rhs_over_lhs)
    
    
    def _perform_simplex_step(self, ):
        values_pivot_column = self.tab[:, self.pivot_column]
        pivot_column_vector = np.reshape(values_pivot_column, 
                                         (len(values_pivot_column), 1))
        
        handled_pivot_row = (self.tab[self.pivot_row,:] / 
                             self.tab[self.pivot_row, self.pivot_column])
        pivot_row_vector = np.reshape(handled_pivot_row, 
                                      (1, len(handled_pivot_row)))
        
        diff = pivot_column_vector * pivot_row_vector
        
        self.tab -= diff
        self.tab[self.pivot_row, :] = handled_pivot_row
    
    
    def _read_solution(self, ):
        """ 
        Solution variables have entries in the final row of the tableau that
        are equal to zero. Furthermore, the corresponding vector only has
        one entry unequal to zero. Such variables form a basis, all other 
        variables are zero.        
        """
        solution = np.zeros(self.tab.shape[1] - 1)
        
        for column in range(len(solution)):
            if self.tab[-1, column] == 0:
                current_vector = self.tab[:-1, column]
                if sum(self.tab[:-1, column] != 0) == 1:
                    row = np.argmax(np.abs(current_vector))
                    solution[column] = self.tab[row, -1] / self.tab[row, column]
        
        return solution