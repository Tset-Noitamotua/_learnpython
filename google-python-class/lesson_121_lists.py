# -*- coding: utf-8 -*-
# filename: lesson_121_list.py
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

# LIST METHODS
# usage: LIST.METHOD(ARGUMENTs)
# L.append(ELEMENT)           ---> append ELEMENT as is at the end of list L
# L.extend('LIST')            ---> add elements of LIST at the end of L
# L.insert(INDEX, 'ELEMENT')  ---> insert ELEMENT at INDEX e.g. 0 of L
# L.remove('ELEMENT')         ---> search and remove ELEMENT from L
# L.pop()                     ---> remove and return LAST element from L
# L.pop(INDEX)                ---> remove and return given INDEX from L
# L.index('ELEMENT')          ---> return the INDEX of ELEMENT in L
# NOTE: Common error - the above methods do not RETURN the modified list,
#       they just modify it!!!

L = ['larry', 'curly', 'moe']
print(L)
# appends the given list as is to L
L.append(['Tset', 'Noitamotua'])
print(L)
# appends each string and number from given list to L
L.extend(['TESTER', 'QA', 1, 3, 'PASS'])
print(L)
# inserts string PROWSER at index 0 of L
L.insert(0, 'PROWSER')
print(L)
L.remove('larry')
print(L)
# removes last element of L (index (-1) -> PASS) and returns it
L.pop()
print(L)
# removes first element (PROWSER) and returns it
L.pop(0)
print(L)

# Example of common mistake mentioned above
try:
    a = L.append(99)
    print('a ---> ' + str(a))
    if a == None:
        print('What did I told you above, BITCH?!')
        print('List methods do NOT return the modified list!')
        print("They just modify it! But they don't RETURN it!")
        print("That's why a is None!!!")
        print('But the list was modified, though:')
        print(L)
except:
    raise
