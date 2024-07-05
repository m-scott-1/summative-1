# test.py

"""
Testing at module level

To run in terminal: python -m doctest -v app.py
More info: 
"""

import doctest
import utils

doctest.testmod(utils)