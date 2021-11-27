import sqlite3
db = sqlite3.connect('db/database.db')
cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS AreaArea( id INTEGER PRIMARY KEY , idunity INTEGER, idParentArea INTEGER, idChildArea INTEGER)""")
db.commit()




def AddUnion (idUnion, idParentArea , idChildArea ):
 cursor.execute("INSERT INTO AreaArea VALUES (NULL,  ? , ? , ? )", (idUnion, idParentArea, idChildArea ))
 db.commit()

def DeleteUnion (idUnion):
 cursor.execute(""" DELETE FROM AreaArea WHERE idunity = ? """, (idUnion,))
 db.commit()

def OutPut():
 select_all_rows = "SELECT * FROM AreaArea "
 cursor.execute(select_all_rows)
 rows = cursor.fetchall()
 return rows 

while  True:

    
 print(
     'Выбирите действие которое хотите сделать : 1) плюс - добавить соединение : '
     'минус - убрать соединение : '
     ' звёздочка для вывода всей таблицы на экран : '
      )

     
 chosen = input()
   
 if(chosen != '+'  and chosen != '-' and chosen != '*'): 
     print('Неверная  команда, попробуйте  ещё :)')
 else : break
   


if (chosen == '+'):
     idUnion = int(input(' Введите id  соединения : '))
     idParentArea= int(input(' Введите id материнской области : '))
     idChildArea = int(input(' Введите id дочерней области : '))
     AddUnion(idUnion,idParentArea,idChildArea)


elif (chosen == '-'):

 idUnion = int(input(' Введите id  соединения чтобы удалить его  : '))
 DeleteUnion(idUnion)


elif (chosen == '*'):
     rows = OutPut ()
     for row in rows:
        print(row)
        
db.commit()
db.close()
