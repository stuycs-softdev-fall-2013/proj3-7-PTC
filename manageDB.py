#!usr/bin/python

import sqlite3

def insertTeacher(name, room):
    database = sqlite3.connect('ParentTeacher.db')
    database.execute('''
    CREATE TABLE if not exists TEACHERS(NAME text, ROOM text)
''')
    database.execute ('''INSERT INTO TEACHERS 
    (NAME, ROOM) \
    VALUES (?, ?)''',[name, room])
    database.commit()
    database.close()

def insertParent(name, sid):
    database = sqlite3.connect('ParentTeacher.db')
    database.execute('''
    CREATE TABLE if not exists PARENTS(NAME text, ID text)
''')
    database.execute ('''INSERT INTO PARENTS 
    (NAME, ID) \
    VALUES (?, ?)''',[name, sid])
    database.commit()
    database.close()

def getTeacherSchedule(name):
    database = sqlite3.connect("ParentTeacher.db")
    q = '''SELECT TIME, PARENT FROM TEACHER 
    WHERE NAME = ?'''
    cursor = database.execute(q, [name])
    time = cursor[0]
    parent = cursor[1]
    database.commit()
    database.close()

def getParentSchedule(name):
    database = sqlite3.connect("ParentTeacher.db")
    q = '''SELECT TIME, TEACHER FROM PARENT
    WHERE NAME = ?'''
    cursor = database.execute(q, [name])
    time = cursor[0]
    teacher = cursor[1]
    database.commit()
    database.close()

def scheduleUpdate(parentName, teacherName, time):
    database = sqlite3.connect("ParentTeacher.db")
    t = '''SELECT TIME, PARENT FROM TEACHER 
    WHERE NAME = ?'''
    cursorT = database.execute(t, [name])
    p = '''SELECT TIME, TEACHER FROM PARENT
    WHERE NAME = ?'''
    cursorP = database.execute(p, [name])
    timeT = cursorT[0].append(time)
    parent = cursorT[1].append(parentName)
    timeP = cursorP[0].append(time)
    teacher = cursorP[1].append(teacherName)
    
    p = '''UPDATE PARENT
    set TIME = ?, TEACHER = ?
    WHERE NAME = ?'''
    database.execute(p [timet, teacher, parentName])
    t = '''UPDATE TEACHER
    set TIME = ?, PARENT = ?
    WHERE NAME = ?'''
    database.execute(t, [timeP, parent, teacherName])
    database.commit()
    database.close()
    
