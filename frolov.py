import sqlite3

con = sqlite3.connect('an.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS a2(
    id INT PRIMARY KEY,
    ans TEXT);
""")
con.commit()

def dob():
    try:
        con = sqlite3.connect('an.db')
        cur = con.cursor()
        an = ('5','16:20')

        cur.execute("INSERT OR IGNORE INTO a2 VALUES(?, ?);", an)
        con.commit()
    except sqlite3.Error as error:
         print(error)
    finally:
         if con:
            con.close()
            print("end")


def viv_one():
    try:
        con = sqlite3.connect('an.db')
        cur = con.cursor()

        cur.execute("SELECT*FROM a2;")
        print(cur.fetchone())

    except sqlite3.Error as error:
             print(error)
    finally:
         if con:
            con.close()
            print("end")

def viv_many():
    try:
        con = sqlite3.connect('an.db')
        cur = con.cursor()

        cur.execute("SELECT*FROM a2;")
        print(cur.fetchmany(3))

    except sqlite3.Error as error:
             print(error)
    finally:
         if con:
            con.close()
            print("end")

def viv_all():
    try:
        con = sqlite3.connect('an.db')
        cur = con.cursor()

        cur.execute("SELECT*FROM a2;")
        print(cur.fetchall())

    except sqlite3.Error as error:
             print(error)
    finally:
         if con:
            con.close()
            print("end")

def del_1():
    try:
        con = sqlite3.connect('an.db')
        cur = con.cursor()

        cur.execute("""DELETE FROM a2 WHERE id='1';""")
        con.commit()
        
    except sqlite3.Error as error:
             print(error)
    finally:
         if con:
            con.close()
            print("end")


viv_all()

    
