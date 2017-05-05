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

class DefectModel:
    """
    The DefectModel class describes model of a defect.
    """
    def get_defect_list(self, component):
        pass

# Connection to SQLite3 DB (local file test.db)
con = lite.connect('test.db')

def main():
    
    with con:
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print('SQLite Version: %s' % data)

        # create table in db
        try:
            cur.execute('CREATE TABLE Cars(Id INT, Name TEXT, Price INT)')
        except lite.OperationalError, error:
            print(error)
        # insert data into db
        cur.execute('INSERT INTO Cars VALUES(1, "Audi", 52642)')
        cur.execute('INSERT INTO Cars VALUES(2, "Mercedes", 57127)')
        cur.execute('INSERT INTO Cars VALUES(3, "Skoda", 9000)')
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")


if __name__ == '__main__':
    main()
