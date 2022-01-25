import sqlite3

#область-область
db = sqlite3.connect('database.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS AreaArea( id INTEGER PRIMARY KEY , idParentArea INTEGER, idChildArea INTEGER)""")
db.commit()

def dob_in_area_area ( idParentArea , idChildArea ):
 cur.execute("INSERT INTO AreaArea VALUES (NULL, ? , ? )", ( idParentArea, idChildArea))
 db.commit()

def del_in_area_area (id):
 cur.execute(""" DELETE FROM AreaArea WHERE id = ? """, (id,))
 db.commit()

def viv_in_area_area():
 cur.execute("SELECT * FROM AreaArea ;")
 print(cur.fetchall())


"""while True:
 print(
 'Выбирите действие которое хотите сделать : 1) плюс - добавить соединение : '
 'минус - убрать соединение : '
 ' звёздочка для вывода всей таблицы на экран : '
 )
 chosen = input()
 if(chosen != '+' and chosen != '-' and chosen != '*'):
  print('Неверная команда, попробуйте ещё :)')
 else : break
if (chosen == '+'):
 idParentArea= int(input(' Введите id материнской области : '))
 idChildArea = int(input(' Введите id дочерней области : '))
 AddUnion(idParentArea,idChildArea)
elif (chosen == '-'):
 id = int(input(' Введите id соединения чтобы удалить его : '))
 DeleteUnion(id)
elif (chosen == '*'):
 rows = OutPut ()
 for row in rows:
  print(row)"""


db.commit()


#область-вопрос       
cur.execute("""CREATE TABLE IF NOT EXISTS Area(idAreas INTEGER,Name TEXT, FOREIGN KEY (idAreas) REFERENCES Area_question (idAreas))""")
db.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Area_question(id INTEGER PRIMARY KEY, idAreas INTEGER, idQuestions INTEGER)""")
db.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Question (idQuestions INTEGER, Question TEXT, FOREIGN KEY (idQuestions) REFERENCES Area_question (idQuestions))""")
db.commit()

def dob_in_area_question(idAreas,idQuestions):
    Area_question = idAreas,idQuestions
    cur.execute("INSERT INTO 'Area_question' VALUES (NULL,?,?)",(Area_question))
    db.commit()

def viv_in_area_question():
    cur.execute("SELECT * FROM Area_question;")
    print(cur.fetchall())

def del_in_area_question(d):
    cur.execute("""DELETE FROM Area_question WHERE id = ? """,(d))
    db.commit()

#вопрос-ответ
cur.execute("""CREATE TABLE IF NOT EXISTS qwestion_answer(id INT PRIMARY KEY, qwestion TEXT, answer TEXT)""")
db.commit()

def dob_in_question_answer (id,question,answer):
    question_answer = id,question,answer
    cur.execute("INSERT INTO 'qwestion_answer' VALUES (?, ?, ?);", (question_answer))
    db.commit()

def viv_in_question_answer():
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchall())

def del_in_question_answer(i):
    cur.execute("""DELETE FROM qwestion_answer WHERE id = ? """,(i))
    db.commit()


db.close()
