# -*- coding: utf-8 -*-
# filename: lesson_122_list_methods.py
# Life is short, use Python!

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
# get an element's index
print(L.index('curly'))
print(L.index(['Tset', 'Noitamotua']))
print(L.index('TESTER'))

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
