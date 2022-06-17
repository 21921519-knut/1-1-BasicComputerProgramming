'''
import sqlite3

c = sqlite3.connect("lecture1")
cursor = c.cursor()

#cursor.execute("delete from student")
cursor.execute("drop table student")

c.commit()
c.close()
'''

import sqlite3

con = sqlite3.connect("lecture1")
cur = con.cursor()

cur.execute("insert into student values (3, '1726103','이순신','010',24)")
cur.execute("insert into student values (4, '1726105','세종대왕','011',29)")

con.commit()
con.close()
