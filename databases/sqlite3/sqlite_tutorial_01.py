# -*- coding: utf-8 -*-
"""
sqlite_tutorial_01.py

This is code from online "SQLite Python tutorial": http://zetcode.com/db/sqlitepythontutorial/

@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""


import sqlite3 as lite
import sys


# Connection to SQLite3 DB (local file test.db)
con = None

def main():

    try:
        con = lite.connect('test_01.db')
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print('SQLite version: %s' % data)
    except lite.Error as e:
        print('SQLite Error %s:' % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    main()
