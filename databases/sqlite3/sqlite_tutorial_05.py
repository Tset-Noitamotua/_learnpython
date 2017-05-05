# -*- coding: utf-8 -*-
"""
sqlite_tutorial_04.py

This is code from online "SQLite Python tutorial": http://zetcode.com/db/sqlitepythontutorial/

@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""

import sqlite3 as lite
import sys


def main():
    try:
        con = lite.connect('test_05.db')

        cur = con.cursor()  
        # use executescript to execute the whole SQL code in one step.
        cur.executescript("""
            DROP TABLE IF EXISTS Cars;
            CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
            INSERT INTO Cars VALUES(1,'Audi',52642);
            INSERT INTO Cars VALUES(2,'Mercedes',57127);
            INSERT INTO Cars VALUES(3,'Skoda',9000);
            INSERT INTO Cars VALUES(4,'Volvo',29000);
            INSERT INTO Cars VALUES(5,'Bentley',350000);
            INSERT INTO Cars VALUES(6,'Citroen',21000);
            INSERT INTO Cars VALUES(7,'Hummer',41400);
            INSERT INTO Cars VALUES(8,'Volkswagen',21600);
            """)

        con.commit()
        
    except lite.Error as e:
        
        if con:
            con.rollback()
            
        print("Error %s:" % e.args[0])
        sys.exit(1)
        
    finally:
        
        if con:
            con.close()


if __name__ == '__main__':
    main()
