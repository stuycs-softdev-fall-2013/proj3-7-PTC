#!usr/bin/python

import sqlite3

#sqlite3 ParentTeacher.db

conn = sqlite3.connect("ParentTeacher.db")

conn.execute('''CREATE TABLE TEACHERS
(NAME TEXT PRIMARY KEY,
ROOM INT,
TIME TEXT,
PARENT TEXT);''')

conn.execute('''CREATE TABLE PARENTS
(NAME TEXT PRIMARY KEY,
ID INT,
TIME TEXT,
TEACHER TEXT);''')

conn.commit()
conn.close()