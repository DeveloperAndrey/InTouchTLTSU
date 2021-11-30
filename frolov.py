import sqlite3

con = sqlite3.connect('an.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS qwestion_answer(
    id INT PRIMARY KEY,
    qw TEXT,
    ans TEXT);
""")
con.commit()

def dob (i,q,a):
    data_base = i,q,a
    cur.execute("INSERT OR IGNORE INTO qwestion_answer VALUES(?, ?, ?);", data_base)

    con.commit()

def viv_many(k):
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchmany(k))


def viv_all():
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchall())



def del_1(i):
    d = ("""DELETE FROM qwestion_answer WHERE id = ? """)
    cur.execute(d,(i,))
    con.commit()


viv_all()
