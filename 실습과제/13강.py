#과제 1
'''
import sqlite3

mydb = sqlite3.connect("lecture3")
cur = mydb.cursor()
#cur.execute("drop table member")
cur.execute("create table member (id str, name varchar(20), email str,birth int)")

mydb.commit()
mydb.close()
'''
#과제 2
'''
import sqlite3

mydb = sqlite3.connect("lecture3")
cur = mydb.cursor()

cur.execute("insert into member values ('hong', '홍길동', 'hong@i.a.k', 1990)")

mydb.commit()
mydb.close()
'''
#과제 3
'''
import sqlite3

mydb = sqlite3.connect("lecture3")
cur = mydb.cursor()

cur.execute("select * from member")
record = cur.fetchone()
print(record[0],record[2])
mydb.commit()
mydb.close()
'''
#과제 4
''''
import sqlite3

mydb = sqlite3.connect("lecture3")
cur = mydb.cursor()

flag = True

while flag != False :
    lst = []
    a = input("아이디 : ")
    if a == '' :
        flag = False
        break
    b = input("이름 : ")
    c = input("이메일 : ")
    d = input("출생년도 : ")
    cur.execute("insert into member values ('"+a+"','"+b+"','"+c+"',"+d+")")

mydb.commit()
mydb.close()
'''
#과제 5
'''
import sqlite3

mydb = sqlite3.connect("lecture3")
cur = mydb.cursor()

cur.execute("select * from member where birth>1999")
record = cur.fetchone()
while record != None :
    print(record[0],record[1],record[3])
    record = cur.fetchone()

mydb.commit()
mydb.close()
'''
