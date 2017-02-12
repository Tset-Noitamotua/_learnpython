# -*- coding: utf-8 -*-
# filename: lesson_123_list_custom_sorting.py

a = ['cccz', 'bb', 'zzzb' 'ZZZa', 'zzz', 'zzza', 'spam', 'foo']

print('a: ' + str(a))

# custom sorting
# using build-in function sorted()
# check help(sorted) to see what arguments sorted() takes
# >>> sorted(iterable, key=None, reverse=False)
# 1. argument is mandatory and can be e.g. a list
# 2. and 3. arguments are optional
# 3. arg we already know. It can be used to reverse the sorting
# 2. arg will allow us to make a custom sorting

# Let's say we want to sort strings in 'a' depending on their last character
# For that we create a function Last(s) which takes a string and returns it's
# last character
def Last(s):
    return s[-1]

# Then we pass that function as 'key' argument to sorted() function
print(sorted(a, key=Last))
print(sorted(a, key=Last, reverse=True))
