import sqlite3
conn = sqlite3.connect("student_info.db")
cursor = conn.cursor()
cursor.execute('''
    create table if not exists student (
        name text not null,
        regno varchar[10] primary key,
        email text not null,
        phno varchar[15] not null
        )
               
    ''')
res=cursor.execute('''
    select * from student
    ''')
print(res.fetchall()
      )
conn.commit()
cursor.close()
