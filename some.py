import sqlite3 

db =   sqlite3.connect('db/database.db')#cursor
cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS  ADMINS ( id INTEGER PRIMARY KEY ,  idtelegram INTEGER  )""")
db.commit()

superAdmin = [ 1111, 43434, 4546546454, 45343543 ,4656453]

def output  () :
    select_all_rows = "SELECT * FROM ADMINS "
    cursor.execute(select_all_rows)
    rows = cursor.fetchall()
    return rows

def AddAdmin (idtelegram):
 cursor.execute("INSERT INTO ADMINS VALUES (NULL,  ?)", (idtelegram, ))
 db.commit()

def DeleteAdmin (idp):
 cursor.execute(""" DELETE FROM ADMINS WHERE idtelegram = ? """, (idp,))
 db.commit()

    
def SelectIdAdmin():
    select_all_rows = "SELECT idtelegram FROM ADMINS "
    cursor.execute(select_all_rows)
    idAdmin = cursor.fetchall()
    return idAdmin

async def checksuperadmin(fn):
    async def wrapped(message):
         if message.user.id in superAdmin :
              return  await fn(message)       
    return wrapped
        
async def checkadmin(fn):
    async def wrapped(message):
         for row in SelectIdAdmin():
          if  (myid == row[0]):
           return  await fn(message) 
                  
    return wrapped

while  True:
 print(' Введите свой id телеграмма : ')
 myid = int(input())
    
 print(
     'Выбирите действие которое хотите сделать : 1) плюс - добавить пользователя : '
     'минус - убрать пользователя : '
     ' звёздочка для вывода всей таблицы на экран : '
      )

     
 chosen = input()
   
 if(chosen != '+'  and chosen != '-' and chosen != '?' and chosen != '*'): 
     print('Неверная  команда, попробуйте  ещё :)')
 else : break
   


if (chosen == '+'):
     idtelegram = int(input(' Введите id пользователя телеграмма : '))
     AddAdmin(idtelegram)


elif (chosen == '-'):

 idp = int(input(' Введите id  пользователя чтобы удалить пользователя по его телеграмм id : '))
 DeleteAdmin(idp)
        

elif (chosen == '*'):
     rows = output ()
     for row in rows:
        print(row)
     


db.commit()
db.close()





