# -*- coding: utf-8 -*-
"""
sqlite_tutorial_02.py

This is code from online "SQLite Python tutorial": http://zetcode.com/db/sqlitepythontutorial/

@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""


import sqlite3 as lite
import sys


# Connection to SQLite3 DB (local file test.db)
con = lite.connect('test_02.db')

def main():
    
    with con:
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print('SQLite Version: %s' % data)
    
    # NOTE: the 'with' part above replaces the 'try - expect' part below
    # try:
    #     con = lite.connect('test.db')
    #     cur = con.cursor()
    #     cur.execute('SELECT SQLITE_VERSION()')
    #     data = cur.fetchone()
    #     print('SQLite version: %s' % data)
    # except lite.Error, e:
    #     print('Error %s:' % e.args[0])
    #     sys.exit(1)
    # finally:
    #     if con:
    #         con.close()


if __name__ == '__main__':
    main()
