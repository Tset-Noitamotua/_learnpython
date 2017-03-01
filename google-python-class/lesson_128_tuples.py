# -*- coding: utf-8 -*-
# https://developers.google.com/edu/python/sorting#tuples
# filename: lesson_124_lists_looping.py

"""NOTE: To create a tuple, just list the values within parenthesis separated by commas. The "empty" tuple is just an empty pair of parenthesis. Accessing the elements in a tuple is just like a list -- len(), [ ], for, in, etc. all work the same.
"""
tuple = (1, 2, 'hi')
print(tuple)
print(len(tuple))  ## 3
print(tuple[2])    ## hi
try:
    tuple[2] = 'bye'  ## NO, tuples cannot be changed
except TypeError:
    print('NO, tuples cannot be changed!')
tuple = (1, 2, 'bye')  ## this works
print(tuple)


"""NOTE: To create a size-1 tuple, the lone element must be followed by a comma.
Why? The comma is necessary to distinguish the tuple from the ordinary case of putting an expression in parentheses.
"""
tuple = ('hi',)   ## size-1 tuple
print(tuple)