import sqlite3

conn = sqlite3.connect("areas-question.db")
cursorObj = conn.cursor()


from sqlite3 import Error

def sql_connection():


    try:

        conn = sqlite3.connect(':memory:')

        return conn

    except Error:

        print(Error)

def sql_table(conn):

    cursorObj = conn.cursor()


    cursorObj.execute("CREATE TABLE id areas(id integer PRIMARY KEY,name text,salary real, position text, hireDate text)")

    cursorObj = conn.cursor()

    conn.commit()

    cursorObj.execute("CREATE TABLE id question(id integer PRIMARY KEY, name text, salary real, position text, hireDate text)")


    conn.commit()


conn = sql_connection()
sql_table(conn)


conn.close()



     
