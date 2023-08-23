import sqlite3

### sakht ya vasl shodan be database, va sakht table dar on:

# be databaes vasl mishe v age nabashe, misaze.
conn = sqlite3.connect('database.db')

# cursor bara anjam kar hast.
cur = conn.cursor()

# harkari ra, ba "execute" anjam midahim.
# sakht table daron database va radif haye on, be shekl zir:
cur.execute("""CREATE TABLE table_name (
first_name text,
last_name text,
email text,
age integer
)""")

# DATATYPES:
# text = str
# integer = int
# real = float
# null = does it exist,or not.
# blob = mp3,jpeg &...

# bara ejra dastoor cursor, bayad connection khod ro "commit" konim.
conn.commit(

)
# va on ra bebandim
conn.close()



### zakhire dade dar database:

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# yek list az tuple misazim ba tavajo be radif haye table:

info = [
    ('yazdan','burning','mail@gmail.com','17'),
    ('micheal','freezing','micheal.mail@gmail.com','24')
]

# be shekl zir on ra dar table database khod zakhire mikonim
cur.executemany("INSERT INTO table_name VALUES (?,?,?,?)", info)

# baraye inke faqad 1 radif dar table vared konim:
cur.execute("INSERT INTO table_name VALUES ('mohsen', 'kolivand', 'mohseln.kol@gmail.com', 998776655)")


conn.commit()
conn.close()

### baraye barresi didane table:

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# "*" yani kole dadeha.
cur.execute("SELECT * FROM table_name")

items = cur.fetchall()

print(items)

conn.commit()
conn.close()

### rowid

# har radif, yek "rowid" darad ke ba farakhandan on,namayan mishavad

conn = sqlite3.connect('database.db')
cur = conn.cursor()


cur.execute("SELECT rowid, * FROM table_name")

items = cur.fetchall()

print(items)

conn.commit()
conn.close()

### search baraye 1 dade khas

cur.execute("SELECT * FROM table_name WHERE sen < 20")
# ya:
cur.execute("SELECT * FROM table_name WHERE first_name like = 'yaz%'")

item = cur.fetchall()

print(item)

### update records:

cur.execute("""UPDATE table_name SET age = 59 
               WHERE first_name = 'alireza'
""")

# or
# in behtare chon eshtebah pish nmiad
cur.execute("""UPDATE table_name SET age = 59 
               WHERE rowid = 3
               """)

# or _ and

cur.execute("UPDATE table_name SET email = 'bibobibobibobibobibo' "
            "WHERE first_name LIKE '%a%' and rowid > 2")

conn.commit()

cur.execute("SELECT rowid, * FROM table_name")

items = cur.fetchall()

for item in items:
    print(item)

conn.commit()
conn.close()

### deleting records
cur.execute("DELETE FROM table_name WHERE first_name = 'yazdan'")

### ordering
cur.execute("SELECT rowid, * FROM table_name ORDER BY rowid desc")
# or
cur.execute("SELECT rowid, * FROM table_name ORDER BY first_name")#alphabet

### limiting result
# age donbal chizi bashid v database kheili bozorgi dashte bashid,
# ba "limit", mitavanid faqad tedad moshakhasi result begirid:
cur.execute("SELECT rowid, * FROM table_name LIMIT 3")

### delete or drop a table:
cur.execute("DROP TABLE table_name")
conn.commit()
