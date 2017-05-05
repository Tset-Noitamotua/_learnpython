# SQLite3 Python Tutorial

Follow this cool tutorial online [SQLite3 Python Tutorial][1]!

[1]: http://zetcode.com/db/sqlitepythontutorial/

## Prerequisites
1. Python 2.7 / 3.5+???
3. SQLite3 [command line tools][2]

[2]: https://sqlite.org/download.html

## Usage
Just run each .py file with Python on your command line, e.g.:

```bash
python sqlite_tutorial_01.py
```
This will create a local .db file (e.g. test_01.db).

Use sqlite command line tool to examine created db, e.g.:

```bash
sqlite3 test_03.db
.mode column
.headers on
SELECT * FROM Cars
```
