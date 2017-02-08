# -*- coding: utf-8 -*-
# filename: lesson_005_if_else.py

import sys

def hello(name):
    if name == 'wlad' or name == 'tset':
        name = name + '!!!'
        print('Hello %s' % (name).capitalize())
    else:
        name = name + '!'
        print('Bey Bey %s' % (name).capitalize())

def main():
    hello((sys.argv[1]).lower())


if __name__ == '__main__':
    main()