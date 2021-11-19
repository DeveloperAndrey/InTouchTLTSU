import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='ru')
inp = input()
output = []
qalist1 = []
tags = ['обед','расписание']  # вместо tags будет просто прикреплена область из бд
qa = {"в обед": "когда обед", "будет": "расписание"}
keyword = inp.split()
for i in keyword:
    output.append((str(morph.normal_forms(i)[0])))
for i in qa:
    qalist = qa[i].split()
    qalist1 += qalist
try:
    if len(qa)>len(qalist1):
        for i in range(len(qalist1)):
            for k in range(len(qa)):
                if qa[i] == qalist1[k]:
                    print(f"Нужное слово нашлось {qalist1[k]}")
                    break
    else :
        for i in range(len(qa)):
            for k in range(len(qalist1)):
                if qalist1[i] == qa[k]:
                    print(f"Нужное слово нашлось {qa[k]}")
                    break

except:
    print("eror 404 key eroro ты дурак")
# сравнинвать по буквам и позициям имея какой то счётчик
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# попробовать через колекции