import sqlite3
        
db = sqlite3.connect('Area-question.db')
cur = db.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Area(idAreas INTEGER,Name TEXT )""")
db.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Area_question(id INTEGER PRIMARY KEY, idAreas INTEGER, idQuestions INTEGER)""")
db.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Question (idQuestions INTEGER, Question TEXT)""")
db.commit()


cur.execute("INSERT INTO 'Area_question' VALUES (NULL, '1','7')")
db.commit()

select_all_rows = "SELECT * FROM 'Area_question'"
cur.execute(select_all_rows)
rows = cur.fetchall()


sql = "DELETE FROM Area_question WHERE idAreas = '1'"

cur.execute(sql)
db.commit()


db.close()


