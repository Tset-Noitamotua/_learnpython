# -*- coding: utf-8 -*-
# filename: lesson_008_strings.py
#
# stings are imutable - means they never change!!!
"""
String slicing

Stings are indexed starting from 0 (zero)

 H  E  L  L  O
 0  1  2  3  4
-5 -4 -3 -2 -1

>>> a = 'HELLO'
The first number marks the start of slice, the second marks the end of slice
[start_at : end_before]
[from x : to n (not including n)]
NOTE: 5 marks the end of slice but is NOT included in the slice itself! 
>>> a[0:5]
> 'HELLO
>>> a[0:5] == a[:]
> True
>>> a[0:5] == a[0:]
> True
>>> a[0]
> 'H'
>>> a[-1]
> 'O'
>>> a[1:3]
> 'EL'
>>> a[-5:-3]
> 'HE'
>>> a[-5:-1]
> 'HELL'
>>> a[-5:0]
> ''
>>> a[-5:5]
> 'HELLO'

"""


a = 'HELLO'
b = 'World'
c = '!'

def print_all_string_methods():
    """In Python strings are objects (like everything else, too)!
This function shows all methods that you can use on string objects.
This methods also called build-in functions.

To get help on each string method you can do this in interactive console:
help(''.<name of string method>)
e.g. help('xyz'.split) is the same as calling help(str.split)

EXAMPLE
>>> help(''.upper)
> Help on built-in function upper:
> upper(...)
>    S.upper() -> string
>
>    Return a copy of the string S converted to uppercase.
> (END)
    """
    print('\n======== build-in functions of string objects =======\n')
    print(dir(a))
    print('\n======== build-in functions of string objects =======\n')

def main():
    print(a)
    # lower case
    print(a.lower())
    # upper case
    print(b.upper())
    print(a, 'You see, original "a" did not changed!')
    # upper case only first character
    print(a.capitalize())
    # show build-in functions of string object
    print_all_string_methods()
    # show help doc of capitalize() function
    print(('string'.capitalize).__doc__)
    # access part of string, here the first character of 'a' only
    print(a[0])
    # here last character of 'a'
    print(a[-1])
    # here characters 0 - 4 (not including 4 - thus 0, 1, 2, 3)
    print(a[0:4])
    # and now including 4
    print(a[0:5])
    # NOTE: Next two examples can be usefull very often!!!
    # if you want to ommit the last n characters  (here 3)
    print(a[:-3])
    # if you want to keep only the last n characters (here 2)
    print(a[-2:])

if __name__ == '__main__':
    main()