import sqlite3

con = sqlite3.connect('an.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS qwestion_answer(
    id INT PRIMARY KEY,
    ans TEXT,
    qw TEXT);
""")
con.commit()

def dob():
    date_base = ('00001','Когда первая пара?','8:30')

    cur.execute("INSERT OR IGNORE INTO qwestion_answer VALUES(?, ?, ?);", date_base)
    con.commit()


def viv_one():
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchone())


def viv_many():
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchmany(3))


def viv_all():
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchall())



def del_1():
    cur.execute("""DELETE FROM qwestion_answer WHERE id='1';""")
    con.commit()

viv_all()

    
