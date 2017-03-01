# -*- coding: utf-8 -*-
# https://developers.google.com/edu/python/dict-files

"""NOTE: A for loop on a dictionary iterates over its keys by default. The keys will appear in an arbitrary order. The methods dict.keys() and dict.values() return lists of the keys or values explicitly. Fortunately one can pass dicts to the sorted() function.
"""

my_dict = {
    'a': 'alpha',
    'b': 'beta',
    'g': 'gamma',
    'o': 'omega'
}
print(my_dict)


# random sorted (default)
print('\nunsorted')
for k in my_dict:
    print(k)

for k in my_dict.keys():  # same as above
    print(k)

print('\nsorted')
# pass dict to sorted() function
for k in sorted(my_dict):
    print(k)

for k in sorted(my_dict.keys()):
    print(k, my_dict[k])

# using enumerate()
print('\nunsorted')
for index, key in enumerate(my_dict):
    print(index, key)

print('\nsorted')
for index, key in enumerate(sorted(my_dict)):
    print(index, key)

# This loop syntax accesses the whole dict by looping
# over the .items() tuple list, accessing one (key, value) pair
# on each iteration.
for k, v in my_dict.items():
    print(k, '>', v)
