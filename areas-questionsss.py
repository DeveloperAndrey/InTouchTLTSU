import sqlite3
        
base = sqlite3.connect('areas-question.db')
cur = base.cursor()


base.execute('CREATE TABLE IF NOT EXISTS {}(id_области INTEGER,Наименование TEXT )'.format('Область'))
base.commit()

cur.execute('INSERT INTO Область VALUES(?, ?)', ('1','Область1'))
base.commit()

base.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER, id_области INTEGER, id_вопроса INTEGER)'.format('Область_вопрос'))
base.commit()

cur.execute('INSERT INTO Область_вопрос VALUES(?, ?, ?)',('1', '11', '11'))
base.commit()

base.execute('CREATE TABLE IF NOT EXISTS {} (id_вопроса INTEGER, Вопрос TEXT)'.format('Вопрос'))
base.commit()

cur.execute('INSERT INTO Вопрос VALUES(?, ?)', ('1','вопрос?'))
base.commit()

cur.execute('SELECT * FROM Область CROSS JOIN Область_вопрос')
base.commit()

cur.execute('SELECT * FROM Вопрос CROSS JOIN Область_вопрос')
base.commit()

rows = cur.execute('SELECT * FROM Область_вопрос').fetchall()
print(rows)

cur.execute('DELETE FROM Область_вопрос')
print('Удалено',cur.rowcount, 'строк')


cur.close()






