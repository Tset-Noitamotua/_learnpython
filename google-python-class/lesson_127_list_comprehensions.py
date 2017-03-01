# -*- coding: utf-8 -*-
# https://developers.google.com/edu/python/sorting#list-comprehensions-optional

# NOTE: A list comprehension is a compact way to write an expression that expands to a whole list

nums = [1, 2, 3, 4]
print(nums)
# list comprehension to compute squares of above list "nums"
squares = [ n * n for n in nums]
print(squares)

"""NOTE: The syntax is [ expr for var in list ] -- the for var in list looks like a regular for-loop, but without the colon (:). The expr to its left is evaluated once for each element to give the values for the new list. Here is an example with strings, where each string is changed to upper case with '!!!' appended:
"""
strings = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strings ]
print(shouting)

"""NOTE: You can add an if test **to the right** of the for-loop to narrow the result. The if test is evaluated for each element, including only the elements where the test is true.
"""
# Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]
print(small)

# Select fruits containing 'a' and change them to upper case
fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [ f.upper() for f in fruits if 'a' in f]
print(afruits)
