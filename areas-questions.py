import sqlite3

base = sqlite3.connect("areas-question.db")
cur = base.cursor()


base.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER,Наименование TEXT )'.format('Область'))
base.commit()

cur.execute('INSERT INTO Область VALUES(?, ?)', ('1','Область1'))
base.commit()

base.execute('CREATE TABLE IF NOT EXISTS {} (id INTEGER, Вопрос TEXT)'.format('Вопрос'))
base.commit()

cur.execute('INSERT INTO Вопрос VALUES(?, ?)', ('1','вопрос'))
base.commit()

base.execute('SELECT score Наименование FROM Область UNION SELECT VALUES type FROM Вопрос')


