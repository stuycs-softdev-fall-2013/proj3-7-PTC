#!usr/bin/python

import sqlite3

def insertTeacher(name, room):
    conn = sqlite3.connect("ParentTeacher.db")
    q = '''INSERT INTO TEACHERS 
    (NAME, ROOM) \
    VALUES (?, ?)'''
    conn.execute(q, [name, room])
    conn.commit()
    conn.close()

def insertParent(name, sid):
    conn = sqlite3.connect("ParentTeacher.db")
    q = '''INSERT INTO PARENTS 
    (NAME, ID) \
    VALUES (?, ?)'''
    conn.execute(q, [name, sid])
    conn.commit()
    conn.close()

def getTeacherSchedule(name):
    conn = sqlite3.connect("ParentTeacher.db")
    q = '''SELECT TIME, PARENT FROM TEACHER 
    WHERE NAME = ?'''
    cursor = conn.execute(q, [name])
    time = cursor[0]
    parent = cursor[1]
    conn.commit()
    conn.close()

def getParentSchedule(name):
    conn = sqlite3.connect("ParentTeacher.db")
    q = '''SELECT TIME, TEACHER FROM PARENT
    WHERE NAME = ?'''
    cursor = conn.execute(q, [name])
    time = cursor[0]
    teacher = cursor[1]
    conn.commit()
    conn.close()

def scheduleUpdate(parentName, teacherName, time):
    conn = sqlite3.connect("ParentTeacher.db")
    t = '''SELECT TIME, PARENT FROM TEACHER 
    WHERE NAME = ?'''
    cursorT = conn.execute(t, [name])
    p = '''SELECT TIME, TEACHER FROM PARENT
    WHERE NAME = ?'''
    cursorP = conn.execute(p, [name])
    timeT = cursorT[0].append(time)
    parent = cursorT[1].append(parentName)
    timeP = cursorP[0].append(time)
    teacher = cursorP[1].append(teacherName)
    
    p = '''UPDATE PARENT
    set TIME = ?, TEACHER = ?
    WHERE NAME = ?'''
    conn.execute(p [timet, teacher, parentName])
    t = '''UPDATE TEACHER
    set TIME = ?, PARENT = ?
    WHERE NAME = ?'''
    conn.execute(t, [timeP, parent, teacherName])
    conn.commit()
    conn.close()
    
