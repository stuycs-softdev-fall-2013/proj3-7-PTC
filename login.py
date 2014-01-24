#!usr/bin/python

import sqlite3
import manageDB.py

def registerParent(username, password, child, parent, sid):
    insertParent(parent, sid)
    conn = sqlite3.connect("ParentTeacher.db")
    conn.execute('''INSERT INTO PARENTLOGIN 
    (USERNAME, PASSWORD, CHILD, NAME, STUDENTID) \
    VALUES (?, ?, ?, ?, ?)''', (username, password, child, parent, sid));
    conn.commit()
    conn.close()
    
def loginParent(username, password):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT PASSWORD FROM PARENTLOGIN
    WHERE USERNAME = ?''', (username));
    if password == cursor[0]:
        pass
    else:
        pass
    
def registerTeacher(username, password, subject, room, teacher, ver):
    insertTeacher(teacher, room)
    conn = sqlite3.connect("ParentTeacher.db")
    conn.execute('''INSERT INTO TEACHERLOGIN 
    (USERNAME, PASSWORD, SUBJECT, ROOM, NAME) \
    VALUES (?, ?, ?, ?, ?)''', (username, password, subject, room, teacher));
    conn.commit()
    conn.close()

def loginTeacher(username, password):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT PASSWORD FROM TEACHERLOGIN
    WHERE USERNAME = ?''', (username));
    if password == cursor[0]:
        pass
    else:
        pass
