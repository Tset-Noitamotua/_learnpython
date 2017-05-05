# -*- coding: utf-8 -*-
"""
mvc.py
My first attempts with OOP and Design Patterns in Python
Code from here: http://kennison.name/files/zopestore/uploads/python/DesignPatternsInPython_ver0.1.pdf
@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""


import sqlite3 as lite
import types
import sys

con = None


class DefectModel:
    """
    The DefectModel class describes model of a defect.
    """
    def get_defect_list(self, component):
        pass

def main():
    try:
        con = lite.connect('test.db')
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print('SQLite version: %s' % data)
    except lite.Error, e:
        print('Error %s:' % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    main()
