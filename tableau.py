# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:31:33 2019

@author: tschu
"""

import numpy as np

class Tableau(object):
    """ Class for creating simplex tableaus """
    
    def __init__(self, ):
        """ Constructor for Tableau class """
        self.__objectives_provided = False
        self.__constraints_provided = False
        self.tab = []
    
    
    def add_objective(self, c, minimize=True):
        """ 
        Add objective coefficients and define the objective's sense
        
        Parameters
        ----------
        c : 1-d array of floats (m entries)
            Objective coefficients, one coefficient for every variable.
            The last entry is a possible constant in the objective function.
        minimize : bool
            True --> minimization problem, False --> maximization problem
        
        Example
        -------
        >>> minimize 2x + 3y - 4
        >>> add_objective([2,3,-4], True)
        """
        c = np.reshape(c, (1, len(c)))
        
        # Minimization problems require inverting the sense of the objective 
        # coefficients
        if minimize:
            c *= -1
        
        if self.__objectives_provided:
            self.tab[-1,:] = c
        else:
            if self.__constraints_provided:
                self.tab = np.vstack((self.tab, c))
            else:
                self.tab = c
        
        self.__objectives_provided = True
        
    
    def add_constraints(self, A, b):
        """ 
        Add constraints satisfying standard form A * x = b 
        
        When defining <= or >= constraints, insert a slack variable to 
        transform to equality constraints.
        
        Parameters
        ----------
        A : 2-d array of float (n rows, m columns)
            Coefficient matrix
        b : 1-d array of float (n rows)
            Right hand side
        """
        b = np.reshape(b, (len(b), 1))
        
        constraints = np.hstack((A, b))    
        
        if self.__objectives_provided:
            self.tab = np.vstack((constraints, self.tab[-1,:]))
        else:
            self.tab = constraints
        
        self.__constraints_provided = True