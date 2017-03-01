# -*- coding: utf-8 -*-
# filename: lesson_122_lists_default_sorting.py

# list of strings
a = ['cccz', 'bb', 'dd', 'zzz', 'adsf', 'spam', 'foo']

# list of numbers
b = [3, 4, 1, 0, 55, 32, 9, 2, 7, 8, 6, 11]

# list with mixed content
c = ['zzz', 1, 9, 0, 'bbb', 'aaa', 'a1', 'z2', '123a', '234a', '123b']

print('a: ' + str(a))
print('b: ' + str(b))
print('c: ' + str(c))

# default sorting
# using the buildin function - sorted()
# check help(sorted) to see what sorted() does and how it works
# sorts a list of strings in alphabetical order
# NOTE: sorted() does not modify the original list! It return a sorted copy of
#       original list.
# NOTE: check the notes about list method 'sort()' at the end of this file!
print(sorted(a))

# sorts a list of numbers from small to large
print(sorted(b))

# sorts mixed list - small numbers first then alphab.
print(sorted(c))

# reversed sorting
print(sorted(a, reverse=True))
print(sorted(b, reverse=True))
print(sorted(c, reverse=True))

# NOTE: there is also a list method sort() which applies to list only
# usage: L.sort() (where L is a list)
# L.sort() does NOT return anything! It modifies the list in place unlike the
# sorted() function which returns a sorted copy of the list!
x = [3, 2, 99, 1, 5, 6, 0, 2]
print(x)
x.sort()
print(x)

# check next lesson for custom sorting
