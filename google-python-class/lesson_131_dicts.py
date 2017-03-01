# -*- coding: utf-8 -*-
# https://developers.google.com/edu/python/dict-files

"""NOTE: A Dictionary or short dict is Python's efficient key/value hash table structure. The contents of a dict can be written as a series of key:value pairs within braces { }, e.g. dict = {key1:value1, key2:value2, ... }. The "empty dict" is just an empty pair of curly braces {}.

NOTE: IMPORTANT!!!
Keys can be of the type String, Number and Tuple.
Values can be of any type.
"""

# create an empty dict (dictionary)
my_dict = {}
print(my_dict)

# create a dict with content
my_dict = {
    'a': 'alpha',
    'b': 'beta',
    'g': 'gamma',
    'o': 'omega'
}
print(my_dict)

# add key-value item to dict
my_dict['d'] = 'delta'
print(my_dict)

# read all keys of a dict
my_dict.keys()  # NOTE: returns list of keys
print(my_dict.keys())
# get the value of a key
print(my_dict['a'])
try:
    print(my_dict['Z'])  # Throws KeyError
except KeyError:
    print('KeyError - "Z" is not present in "my_dict"!')
print(my_dict.get('a'))  # use .get() method
print(my_dict.get('X'))  # NOTE: .get('X') will return None if 'X' is not present
print(my_dict.get('X', 'Not found!'))  # custom messege if key not found

# check if a key is in dict
result = 'a' in my_dict
print('Is there a key "a" in my dict? -->', result)
if 'Z' in my_dict: print(my_dict['Z'])  # Avoid KeyError


# read all values of a dict
my_dict.values()  # NOTE: return list of values
print(my_dict.values())


# read all key-value items of a dict
my_dict.items()  # NOTE: return list of (key, value) tuples
print(my_dict.items())

# using del
# NOTE: We can use del on a dictionary. We pass the key we want to remove. It removes both the key and its associated value. Only one entry can be removed at a time.
colors = {"red" : 100, "blue" : 50, "purple" : 75}
# Delete the pair with a key of "red."
del colors["red"]
print(colors)