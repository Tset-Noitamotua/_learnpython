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
# Connection to SQLite3 DB in memory
conm = lite.connect(':memory:')

cars = (
    (1, 'Audi', 55232),
    (2, 'Mercedes', 57809),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

def main():
    
    with con:
        # create cursor object
        cur = con.cursor()
        # remove Cars table if it already exists
        cur.execute('DROP TABLE IF EXISTS Cars')
        # create new Cars table
        cur.execute('CREATE TABLE Cars(Id INT, Name TEXT, Price INT)')
        cur.executemany('INSERT INTO Cars VALUES(?, ?, ?)', cars)
    
    with conm:
        cur = conm.cursor()
        cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

        last_id = cur.lastrowid
        print("The last id of the inserted row is %d" % last_id)


if __name__ == '__main__':
    main()
