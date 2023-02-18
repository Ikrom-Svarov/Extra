
# словари
s = {
    "key":{"": 12},
    "key":{"value": 12},
    12: 1.6,
    (13,56):['fsg',123]

}
print(s[(13,56)][0])
#
#
# "s = {
#     "key":{"value": 12},
#     "key":{"value": 12},
#     12: 1.6,
#     (13,56):['fsg',123]
#
# }
# d = {
#     'tr':345,
#     765:'fghd'
#
# }
# s["key"] = 'new values'
#
# d1 = {
#     'tr':345,
#     765:'fghd',
#     77:'dfg',
# }
# s["key"] = 'new values'
"""
#print(s.keys())
#print(s.values())
#print(s.items())
#print(len(s))
#a = {**s,**d}
#d.update(s) # чтобы добавить ключ
#del d ['tr'] # удаляет ключ
#print(d.pop("tr")) # удаляет element
#d.clear() # удаляет весь список
#print('tr' in d) # проверить на trye и false
#f = d.copy() # чтобы скопировать
#f = d.deepcopy() # глубокое копирование

#print(d == d1)   print(d != d1) # чтобы сравнивать
#for key, value in d1.items():
 #   print(f'ключ: {key}, значение: {value}')


# множества
set1 = {1,2,3,4}
#print(type(set1)) # чтобы проверить словарь или множества
#print(set1) # дает 4 значения
#print(len(set1)
#set1.add(5)# добавляет значение
#str1 = 'stroka'
#set1.remove(4)# удаляет елемент
#for i in set1:
 #   print(i)
#print(3 in set1) # проверить есть ли 3

