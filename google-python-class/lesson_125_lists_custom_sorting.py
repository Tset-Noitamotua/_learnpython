# -*- coding: utf-8 -*-
# https://developers.google.com/edu/python/sorting
# filename: lesson_123_lists_custom_sorting.py

a = ['cccz', 'bb', 'zzzb' 'ZZZa', 'zzz', 'zzza', 'spam', 'foo']

print('My list named "a":\n' + str(a) + '\n')

# custom sorting
# using build-in function sorted()
# check help(sorted) to see what arguments sorted() takes
# >>> sorted(iterable, key=None, reverse=False)
# 1. argument is mandatory and can be e.g. a list
# 2. and 3. arguments are optional
# 3. arg we already know. It can be used to reverse the sorting
# 2. arg will allow us to make a custom sorting

# EXAMPLE 1 - Custom Sorting with buildin `len()`
# Specifying `len`as key function makes sort by lenght of elements
print('sorting with buildin "len()":')
print(sorted(a, key=len))
print('\n')

# EXAMPLE 2 - Custom Sorting with buildin `str.lower()`
# Specifying `str.lower`as key function is a way to force sorting to treat
#     uppercase and lowercase the same
print('sorting with buildin "str.lower()":')
print(sorted(a, key=str.lower))
print('\n')

# EXAMPLE 3 - Custom Sorting with on function
# Let's say we want to sort strings in list 'a' depending on their last letter
# For that we create a function Last(s) which takes a string and returns it's
# last letter
def Last(s):      # my own function
    return s[-1]  # return last letter of given string

# Then we pass that function as 'key' argument to sorted() function
print('sorting with my own fuction and with same reversed:')
print(sorted(a, key=Last))
print(sorted(a, key=Last, reverse=True))
