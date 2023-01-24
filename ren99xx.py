import sqlite3
import csv

conn=sqlite3.connect("ren99.db")
c = conn.cursor()
c.execute("drop table if exists shiharai")
c.execute("create table shiharai (id int,name char(20),total int,memo char(30))")

with open("ren99.csv","w") as f:
    writer = csv.writer(f)
    a = 0
    
    while a == 0:
        I = int(input("番号 : "))
        N = (input("店名 : "))
        T = int(input("金額 : "))
        M = (input("明細 : "))

        date = [I,N,T,M]
        print(date)

        c.execute("insert into shiharai values(?,?,?,?)",date)
        itr = c.execute("select * from shiharai order by id")

        a = int(input("続行0 終了1 :"))

        if a == 1:
            for i in itr:
                print(i)
            conn.commit()
            a += 1