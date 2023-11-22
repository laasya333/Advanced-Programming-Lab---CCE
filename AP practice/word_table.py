import sqlite3

conn=sqlite3.connect("table.db")
cursor=conn.cursor()
cursor.execute('''
    create table if not exists words(
        id int primary key,
        word text not null
        )
    ''')
conn.commit()
cursor.close()

#list1=[
#     (1,"abc"),
#    (2,"jafkj"),
#    (3,"ass"),
#    (4,"hhhh")
#    ]
#cursor=conn.cursor()
#cursor.executemany('''
#    insert into words(id,word)
#    values(?,?)
#    ''',list1)
#conn.commit()
#cursor.close()

cursor=conn.cursor()
res=cursor.execute('''
    select * from words
    ''')
print(res.fetchall())
conn.commit()
cursor.close()

cursor=conn.cursor()
cursor.execute('''
    alter table words
    add updated_words text
    ''')
conn.commit()
cursor.close()

cursor=conn.cursor()
cursor.execute('''
    update words
    set updated_words=
    where 
