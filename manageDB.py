#!usr/bin/python

import sqlite3

def insertTeacher(name, room):
    conn = sqlite3.connect("ParentTeacher.db")
    conn.execute('''INSERT INTO TEACHERS 
    (NAME, ROOM) \
    VALUES (?, ?)''', (name, room));

def insertParent(name, sid):
    conn = sqlite3.connect("ParentTeacher.db")
    conn.execute('''INSERT INTO PARENTS 
    (NAME, ID) \
    VALUES (?, ?)''', (name, sid));
    conn.commit()
    conn.close()

def getTeacherSchedule(name):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT TIME, PARENT FROM TEACHER 
    WHERE NAME = ?''', (name));
    time = cursor[0]
    parent = cursor[1]
    conn.commit()
    conn.close()

def getParentSchedule(name):
    conn = sqlite3.connect("ParentTeacher.db")
    cursor = conn.execute('''SELECT TIME, TEACHER FROM PARENT
    WHERE NAME = ?''', (name));
    time = cursor[0]
    teacher = cursor[1]
    conn.commit()
    conn.close()

def scheduleUpdate(parentName, teacherName, time):
    conn = sqlite3.connect("ParentTeacher.db")
    cursorT = conn.execute('''SELECT TIME, PARENT FROM TEACHER 
    WHERE NAME = ?''', (name));
    cursorP = conn.execute('''SELECT TIME, TEACHER FROM PARENT
    WHERE NAME = ?''', (name));
    timeT = cursorT[0].append(time)
    parent = cursorT[1].append(parentName)
    timeP = cursorP[0].append(time)
    teacher = cursorP[1].append(teacherName)

    conn.execute('''UPDATE PARENT
    set TIME = ?, TEACHER = ?
    WHERE NAME = ?''', (timeT, teacher, parentName));
    conn.execute('''UPDATE TEACHER
    set TIME = ?, PARENT = ?
    WHERE NAME = ?''', (timeP, parent, teacherName));
    conn.commit()
    conn.close()
    
