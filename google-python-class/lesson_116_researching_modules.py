# -*- coding: utf-8 -*-
# filename: lesson_116_researching_modules.py
# 
# Two options to research what a specific Python module is good for
# You have to enter interactive console (>>> python) to use them both!
# 
# NOTE: You have to import the module you wish to research firt
#       >>> import sys
# 
# 1. dir function
#    It shows all 'symbols' of a module
#    EXAMPLE        dir(<modul_name>)
#    >>> dir(sys)
#    > [ ... 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', ... ]
#
# 2. help function
#    It shows the docstrings (documentation) of a module/class/function etc.
#    EXAMPLE        help(<modulename | functionname | etc>)
#    >>> help(sys.argv)
#        This will show you documentation like below
#        To exit the help press 'q'
""" 
Help on built-in module sys:

NAME
    sys

FILE
    (built-in)

MODULE DOCS
    http://docs.python.org/library/sys

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
...
"""


import sys

print(dir(sys))

help(sys)
