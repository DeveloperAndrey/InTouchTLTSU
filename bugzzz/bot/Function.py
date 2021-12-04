from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton
from config import TOKEN
import sqlite3
#import psycopg2
# админы
db = sqlite3.connect('database.db')#psycopg2.connect(user='username',
#password = 'password',
#host='db',
#port='5432',
#dbname='db')

cur = db.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS  ADMINS ( id INTEGER PRIMARY KEY ,  idtelegram INTEGER  )""")
db.commit()


def add_admin1(idtelegram):
    if not isinstance(idtelegram, int):
        raise Warning('ne int')
    else:
        cur.execute("INSERT INTO ADMINS VALUES (NULL,  ?)", (idtelegram,))
        db.commit()


def list_admin():
    select_all_rows = "SELECT * FROM ADMINS "
    cur.execute(select_all_rows)
    rows = cur.fetchall()
    return rows


def del_admin(id):
    if not isinstance(id, int):
        raise Warning('ne int')
    else:
        cur.execute(""" DELETE FROM ADMINS WHERE id= ? """, (id,))
        db.commit()


def add_que(idQuestions):
    if not isinstance(idQuestions, int):
        raise Warning('ne int')
    cur.execute("INSERT INTO Question VALUES (NULL,  ?)", (idQuestions,))
    db.commit()


def list_que():
    select_all_rows = "SELECT idquestion FROM Question "
    cur.execute(select_all_rows)
    idquestion = cur.fetchall()
    return idquestion


def del_que(id):
    if not isinstance(id, int):
        raise Warning('ne int')
    cur.execute(""" DELETE FROM Question WHERE id = ? """, (id,))
    db.commit()


def add_area(idAreas):
    if not isinstance(idAreas, int):
        raise Warning('ne int')
    else:
        cur.execute("INSERT INTO Area VALUES (NULL,  ?)", (idAreas,))
        db.commit()


def list_area():
    select_all_rows = "SELECT * FROM Area "
    cur.execute(select_all_rows)
    Area = cur.fetchall()
    return Area


def del_area(id):
    if not isinstance(id, int):
        raise Warning('ne int')
    else:
        cur.execute(""" DELETE FROM Area WHERE id = ? """, (id,))
        db.commit()


def add_que_area(idAreas, idQuestions):
    if not isinstance(idAreas, int) or not isinstance(idQuestions, int):
        raise Warning('ne int')
    cur.execute("INSERT INTO Area_question VALUES (NULL,  ? , ? )", (idAreas, idQuestions))
    db.commit()


def list_que_area():
    select_all_rows = "SELECT * FROM Area_question "
    cur.execute(select_all_rows)
    rows = cur.fetchall()
    return rows


def del_que_area(id):
    if not isinstance(id, int):
        raise Warning('ne int')
    cur.execute(""" DELETE FROM Area_question WHERE id = ?  """, (id,))
    db.commit()


def add_area_area(idParentArea, idChildArea):
    if not isinstance(idChildArea, int) or not isinstance(idParentArea, int):
        raise Warning('ne int')
    else:
        cur.execute("""INSERT INTO AreaArea VALUES (NULL, ? , ? )""", (idParentArea, idChildArea))
        db.commit()


def list_area_area():
    select_all_rows = "SELECT * FROM AreaArea "
    cur.execute(select_all_rows)
    rows = cur.fetchall()
    return rows


def del_area_area(id):
    if not isinstance(id, int):
        raise Warning('ne int')
    else:
        cur.execute(""" DELETE FROM AreaArea WHERE id = ? """, (id,))
        db.commit()


def obl_con_que_list(id_1, id_2):
    select_all_rows = ("SELECT * FROM Area_question WHERE idAreas = ? , idQuestions = ?  ", (id_1, id_2))
    cur.execute(select_all_rows)
    rows = cur.fetchall()
    return rows


def id_obl(id_):
    select_all_rows = ("SELECT * FROM Area WHERE id = ?  ", (id_,))
    cur.execute(select_all_rows)
    Id = cur.fetchall()
    return Id


def obl_names(name):
    select_all_rows = ("SELECT * FROM Area WHERE Name = ?  ", (name,))
    cur.execute(select_all_rows)
    Name = cur.fetchall()
    return Name


def obl_con_obl_list():
    select_all_rows = ("SELECT idParentArea, idChildArea FROM AreaArea")
    cur.execute(select_all_rows)
    rows = cur.fetchall()
    return rows


# область-область

cur.execute(
    """CREATE TABLE IF NOT EXISTS AreaArea( id INTEGER PRIMARY KEY , idParentArea INTEGER, idChildArea INTEGER)""")
db.commit()


def dob_in_area_area(idParentArea, idChildArea):
    cur.execute("INSERT INTO AreaArea VALUES (NULL, ? , ? )", (idParentArea, idChildArea))
    db.commit()


def del_in_area_area(id):
    cur.execute(""" DELETE FROM AreaArea WHERE id = ? """, (id,))
    db.commit()


def viv_in_area_area():
    cur.execute("SELECT * FROM AreaArea ;")
    print(cur.fetchall())


db.commit()

# область-вопрос
cur.execute("""CREATE TABLE IF NOT EXISTS Area(id INTEGER PRIMARY KEY, idAreas INTEGER, Name TEXT) """)
db.commit()

cur.execute(
    """CREATE TABLE IF NOT EXISTS Area_question(id INTEGER PRIMARY KEY, idAreas INTEGER, idQuestions INTEGER)""")
db.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Question (id INTEGER PRIMARY KEY, idQuestions INTEGER, Question TEXT)""")
db.commit()


def dob_in_area_question(idAreas, idQuestions):
    Area_question = idAreas, idQuestions
    cur.execute("INSERT INTO 'Area_question' VALUES (NULL,?,?)", (Area_question))
    db.commit()


def viv_in_area_question():
    cur.execute("SELECT * FROM Area_question;")
    print(cur.fetchall())


def del_in_area_question(d):
    cur.execute("""DELETE FROM Area_question WHERE id = ? """, (d))
    db.commit()


# вопрос-ответ
cur.execute("""CREATE TABLE IF NOT EXISTS qwestion_answer(id INT PRIMARY KEY, qwestion TEXT, answer TEXT)""")
db.commit()


def dob_in_question_answer(id, question, answer):
    question_answer = id, question, answer
    cur.execute("INSERT INTO 'qwestion_answer' VALUES (?, ?, ?);", (question_answer))
    db.commit()


def viv_in_question_answer():
    cur.execute("SELECT*FROM qwestion_answer;")
    print(cur.fetchall())


def del_in_question_answer(i):
    cur.execute("""DELETE FROM qwestion_answer WHERE id = ? """, (i))
    db.commit()

