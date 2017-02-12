# -*- coding: utf-8 -*-
# filename: lesson_123_lists_looping.py

my_list = ['Pizza', 'index_1', 'index_2', 'index_3', 'index_4', 'index_5', 
            '1', '2', '3', 'Bannana']

squares = [1, 4, 9, 16]

print('a: ' + str(my_list))

# use 'for' to look at each element in a list
# for-construct: for VAR in LIST
# NOTE: do not modify the list while you iterate through it!

# example 1
for element in my_list:
    print(element)

# example 2
sum = 0
for num in squares:
    sum += num     # same es sum = sum + num
print('sum: ' + str(sum))



# use 'in' to see if an element appears in a list
# in-construct: VALUE in COLLECTION
# a collection can be a list, a dictionary or another iterable

# example 3
if 'Pizza' in my_list:
    print('Yeah, yeah, yeay! I love Pizza!')

print('Burger in my list? --> ' + str('Burger' in my_list))


# use 'for' and 'in' together

# example 4
for i in range(11):
    print(i)

# use 'while' to loop through a list until a condition

# example 5 - access every 2nd element in my_list
i = 0
while i < len(my_list):
    print(str(i) + '. ' + str(my_list[i]))
    i = i + 2

# cool trick to output elements of a list line by line
# WITHOUT using 'for'
# build-in string-method join() is used for that
# usage: S.join(LIST) where S is a delimeter as string e.g. ':', '\n' or what ever
# check >>> help(''.join)
# NOTE: works only if elements are all strings
lines = '\n'.join(my_list)
titel = '\nmy_list line by line:'
print(titel)
print('-' * len(titel))
# NOTE: the output is a string with line breaks
print(lines)

# cool trick to reverse above cool trick
# build-in string-method split() is used for that
# usage: S.split(DELIMETER) where S is the string we wonna split at DELIMETER
new_list = lines.split('\n')
titel = '\nstrings back to list:'
print(titel)
print('-' * len(titel))
# NOTE: the output is a list of strings!
print(new_list)