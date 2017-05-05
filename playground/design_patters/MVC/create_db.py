# -*- coding: utf-8 -*-
"""
create_db.py

This programm will create a SQLite3 DB as local file 'TMS.db'
And populate it with some data which will be used in MVC examples.

@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""

import sqlite3 as lite


data = (
    (1, 'XYZ', 'File does not get deleted'),
    (2, 'XYZ', 'Registry does not get created'),
    (3, 'ABC', 'Wrong title gets displayed')
)

# connect to TMS.db (creates it if it does not already exist)
con = lite.connect('TMS.db')

with con:
    
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Defects")
    cur.execute("CREATE TABLE Defects(Id INT, Component TEXT, Summary TEXT)")
    cur.executemany("INSERT INTO Defects VALUES(?, ?, ?)", data)
