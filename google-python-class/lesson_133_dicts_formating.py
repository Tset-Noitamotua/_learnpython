# -*- coding: utf-8 -*-
# https://developers.google.com/edu/python/dict-files#dict-formatting

# NOTE: The % operator works conveniently to substitute values from a dict into a string by name

dict = {}
dict['word'] = 'girls'
dict['count'] = 99
s = 'I want %(count)d beautiful %(word)s every month!!!' % dict  # %d for int, %s for string
print(s)

# i behind %() stands for integer and s for string
print('I want %(count)i beautiful %(word)s!!!' % dict)

