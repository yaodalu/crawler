# -*- coding: utf-8 -*-
import sqlite3

#创建/打开数据库，存在则打开，不存在则创建
con = sqlite3.connect(r'C:\SQLite\samples\test.db')

#创建游标对象，数据库的查询需要使用到游标对象
cur = con.cursor()
    #execute()用来执行sql语句
    #close()用来关闭游标
    #fetchone()从结果中取出一条记录，并将游标指向下一条记录
    #fetchall()用来取出所有记录
    #scroll用于游标滚动

#使用游标对象创建一个表
cur.execute('CREATE TABLE student(id integer primary key,name varchar(20),age integer)')


#使用占位符‘？’向表中插入数据
cur.execute('INSERT INTO student VALUES (?,?,?)',(0,'QIYE',20))

#插入多条数据
cur.executemany('INSERT INTO student VALUES (?,?,?)',[(1,'yao',20),(2,'lin',18)])

#使用数据库对象进行提交
con.commit()

#查询表中所有数据,并利用fetchall()方法返回数据
cur.execute('SELECT * FROM student')
res = cur.fetchall()
for line in res:
    print line


#修改和删除数据
cur.execute('UPDATE student SET name = ? WHERE id = ?',('rose',1))
cur.execute('DELETE FROM student WHERE id = ?',(0,))

con.commit()
con.close()
