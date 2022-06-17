import sqlite3

con = sqlite3.connect("lecture1")

cur = con.cursor()
#cur.execute("delete from student where num=1726105")
#cur.execute("update student set age=25 where name='홍길동'")
cur.execute("update student set age=age+1")

con.commit()
con.close()
