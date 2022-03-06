import mysql.connector
from tabulate import  tabulate

con = mysql.connector.connect(host="localhost",user="root",password="toor",database="besant")



def insert(b,c):
    r = con.cursor()
    sql = "insert into user1(Name,Course) values (%s,%s)"
    z = (b,c)
    r.execute(sql,z)
    con.commit()

def delete(name):
    r = con.cursor()
    sql = "delete from user1 where Name = %s"
    q = (name,)
    r.execute(sql,q)
    con.commit()
    
def update(a,b):
    r = con.cursor()
    sql = "update user1 set course=%s where Name=%s"
    user = (b,a)
    r.execute(sql,user)
    con.commit()

def select():
    r = con.cursor()
    r.execute("select * from user1")
    a = r.fetchall()
    print(tabulate(a,headers=("name","course")))
    con.commit()



print("""1.INSERT
2.UPDATE
3.DELETE
4.SELECT or show""")
choice = int(input("choice:"))

if choice == 1:
    name = input("name:")
    course = input("course:")
    insert(name,course)
    print("insert completed")

elif choice == 2:
    name = input("name:")
    course = input("course")
    update(name,course)
    print("updated")

elif choice == 3:
    name = input("name:")
    delete(name)
    print("deleted")

elif choice == 4:
    select()
