# -*- coding: utf-8 -*-
# filename: lesson_005_argv.py
#
# sys module
# sys.argv enables you (among other things) to work with arguments 
# e.g. pass arguments from command line to your script
#
# EXAMPLE
# >>> python lesson_005_argv.py arg1 arg2 arg3 xxx
# > ['lesson_005_argv.py', 'arg1', 'arg2', 'arg3', 'xxx']
# > ('0:', 'lesson_005_argv.py')
# > ('1:', 'arg1')
# > ('without 0:', ['arg1', 'arg2', 'arg3', 'xxx'])
# > ('last:', 'xxx')
#
# NOTE: the first arg alway refers to the script itself!!!

import sys

def main():
    print(sys.argv)
    print('0:', sys.argv[0])
    print('1:', sys.argv[1])
    print('without 0:', sys.argv[1:])
    print('last:', sys.argv[-1])


if __name__ == '__main__':
    main()