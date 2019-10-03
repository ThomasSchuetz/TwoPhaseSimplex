# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:25:47 2019

@author: tschu
"""
import sys
sys.path.insert(1, '../src')

import unittest

# import all test scripts
import test_tableau
import test_simplex

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_tableau))
suite.addTests(loader.loadTestsFromModule(test_simplex))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
