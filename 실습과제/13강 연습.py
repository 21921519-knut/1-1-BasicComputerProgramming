
#레코드 문자열 삽입은 반드시 ''로 해라
'''
import sqlite3

con = sqlite3.connect("lecture1")
cur = con.cursor()

cur.execute("create table student (id int, num varchar(10),"+
            "name varchar(20), tel varchar(20), age int)")

cur.execute("insert into student values (1, '1726101','홍길동','010',20)")
cur.execute("insert into student values (2, '1726102','홍길순','011',21)")

con.commit()
con.close()
'''

import sqlite3

con = sqlite3.connect("lecture1")
cur = con.cursor()

cur.execute("select * from student")
record = cur.fetchone()
while record != None :
    print(record[1],record[2],record[3],record[4])
    record = cur.fetchone()

con.commit()
con.close()


