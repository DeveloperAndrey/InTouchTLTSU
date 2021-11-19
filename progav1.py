import pymorphy2
from collections import *

morph = pymorphy2.MorphAnalyzer(lang='ru')
inp = input()
output = []
qalist1 = []
tags = ['обед','расписание']  # вместо tags будет просто прикреплена область из бд
qa = ['когда обед' 'будет', 'расписание', 'Путин Вор', 'путин', 'Ну незнаю', 'знаешь', 'Не заню ходят легенды что это путин', 'кто такой Криштал']
qa_var1 = {'когда обед':'в обед','расписание': 'будет', 'путин':'Путин вор', 'знаешь': 'ну незнаю', 'кто такой криштал': 'Не заню ходят легенды что это путин'}
shish = namedtuple('да','когда обед',)
keyword = inp.split()
for i in keyword:
    output.append((str(morph.normal_forms(i)[0])))
try:
    print(qa_var1[inp.lower()])
except KeyError : print("вы чёта не то ввели давай по новой")












"""
someel = list
for i in range(1,len(qa),2):
    qalist = qa[i].split()
    qalist1.append(qalist)
for  i in range(1,len(qa),2):
    try:
        someel.clear()
    except: pass
    someel = qa[i].split()
    print(qa[i].split())
"""

""""
for k in range(len(qalist1)) :
    c = 0
    if (isinstance(qalist1[k],list)):
        for i in range(len(output)):
            mean = len(qalist1[k]) % 2
            if qalist1[k] == output[i]:
                print(output[i])
                c += 1

            if c >= mean : print(qa[i-1],c,k,i)
"""