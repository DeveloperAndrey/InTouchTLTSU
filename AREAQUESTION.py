import sqlite3
        
db = sqlite3.connect('Area-question.db')
cur = db.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Area(idAreas INTEGER,Name TEXT )""")
db.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Area_question(id INTEGER PRIMARY KEY, idAreas INTEGER, idQuestions INTEGER)""")
db.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Question (idQuestions INTEGER, Question TEXT)""")
db.commit()

def AddWrite(idAreas,idQuestions):
    Area_question = idAreas,idQuestions
    cur.execute("INSERT INTO 'Area_question' VALUES (NULL,?,?)",(Area_question))
    db.commit()

def AddRead(c):
    cur.execute("SELECT * FROM Area_question;")
    print(cur.fetchall())

def Del(d):
    cur.execute("""DELETE FROM Area_question WHERE id = ? """,(d))
    db.commit()



db.close()


