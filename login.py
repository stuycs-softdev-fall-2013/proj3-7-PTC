#!usr/bin/python

import sqlite3
import manageDB

def registerParent(username, password, child, parent, sid):
    manageDB.insertParent(parent, sid)
    conn = sqlite3.connect("ParentTeacher.db")
    conn.execute('''
    CREATE TABLE if not exists PARENTLOGIN(USERNAME text, PASSWORD text, CHILD text, PARENT text, STUDENTID text)
''')
    conn.execute('''INSERT INTO PARENTLOGIN 
    (USERNAME, PASSWORD, CHILD, PARENT, STUDENTID) \
    VALUES (?, ?, ?, ?, ?)''', [username, password, child, parent, sid]);
    conn.commit()
    conn.close()
    
def loginParent(username, password):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT PASSWORD FROM PARENTLOGIN
    WHERE USERNAME = ? and PASSWORD = ?''', [username,password]);
    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False
    
def registerTeacher(username, password, subject, room, teacher, ver):
    manageDB.insertTeacher(teacher, room)
    conn = sqlite3.connect("ParentTeacher.db")
    conn.execute('''
    CREATE TABLE if not exists TEACHERLOGIN(USERNAME text, PASSWORD text, SUBJECT text, ROOM text, NAME text)
''')
    conn.execute('''INSERT INTO TEACHERLOGIN 
    (USERNAME, PASSWORD, SUBJECT, ROOM, NAME) \
    VALUES (?, ?, ?, ?, ?)''', [username, password, subject, room, teacher]);
    conn.commit()
    conn.close()

def loginTeacher(username, password):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT PASSWORD FROM TEACHERLOGIN
    WHERE USERNAME = ? and PASSWORD = ?''', [username,password]);
    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False

def getTeacherName(username):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT NAME FROM TEACHERLOGIN
    WHERE USERNAME = ?''', [username]);
    return cursor.fetchone()[0]

def getParentName(username):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT NAME FROM PARENTLOGIN
    WHERE USERNAME = ?''', [username]);
    return cursor.fetchone()[0] 
