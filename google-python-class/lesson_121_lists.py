# -*- coding: utf-8 -*-
# filename: lesson_121_lists.py
# Life is short, use Python!

# empty list
a = []

# list with content
# NOTE: content can be anything and can also be mixed
a = [1, 2, 3, 'aaa', 'bbb']

# It's common to start with an empty list and then append() or extend() it
list = []          ## Start as the empty list
list.append('a')   ## Use append() to add elements
list.append('b')

# Slices work on lists just as with strings, and can also be used to
# change sub-parts of the list.
list = ['a', 'b', 'c', 'd']
print( list[1:-1] )  ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print( list )        ## ['z', 'c', 'd']

# >>> help(a)   # to see all list methods and further help

# var b points to same object in memory as var a
# NOTE: it does not make a copy of our list a!
b = a

# this will make a copy
b = a[:]    # same as a[0:]
print(a[:] == a[0:])

# this will append two lists
print([1,2] + [3,4])

# accessing content of lists works same as with strings - with index and slices
# REMEMBER [1, 2, 3, 'aaa', 'bbb']
#    index  0  1  2    3      4

# first element of a
print(a[0])

# last element of a
print(a[-1])

# slice: 1 bis 4 ---> index1, index2, index3 (not including index4)
print(a[1:4])      # output: [2, 3, 'aaa']

# lenght of list
print(len(a))

# using del() operator (it is not a function it's an operator!)
print('\nList "a" before using "del()":\n' + str(a))
del a[0]  # delete first element from list
print('\nList "a" after "del a[0] and del[-2]"')
# NOTE: On lists, we can remove slices (ranges of elements) at once.
del a[-2:]  # delete last two elements
print(a)

# TODO: Want even more practical examples?
#       --> https://www.dotnetperls.com/list-python
