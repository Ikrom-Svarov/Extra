# def func(m, g=9.8):
#     return m * g
#
# a = func(m = 56)
# print(a)

# def func(*args):
#     d = args
#     try:
#        for i in d:
#            print(i)
#     except:
#         print('empty list')
#
# func(1,3, 'sde',45)


# f = {
#     'key': 'value'
# }
# def func(**kwargs):
#     d = kwargs
#     try:
#        for i, v in d.items():
#            print(i,v)
#     except:
#         print('empty list')
#
# func(**f)


# def func(**kwargs):
#     d = kwargs
#     try:
#        for i, v in d.items():
#            print(i,v)
#     except:
#         print('empty list')
#
# func(key='123')


# Assert
# def avg(ranks):
#     assert len(ranks) != 0, 'Список ranks не должен быть пустым'
#     return round(sum(ranks)/len(ranks), 2)
#
# ranks = []
# print("Среднее значение:", avg(ranks))


# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x


# a = get_list()
# # print(a)
# for x in a:
#     print(x)



# def get_list():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a)/len(a)
        # for p in a:
        #     print(p, end=' ')
        # print('\n')

# a = get_list()
# print(a)
# print(list(a))



# # инициализация списка
# list_of_nums = [i for i in range(1, 31)]
#
# # вывод начального списка
# print("До фильтрации в генераторе: " + str(list_of_nums))
#
# # вывод только четных значений из списка
# print("Только четные числа: ", end=" ")
# for i in get_even(list_of_nums):
#     print(i, end=" ")


# # Инициализация строки, содержащей текст для поиска
# text = "В Интернете есть множество языков, но python только один. \
#             Программа никогда не прочтет последнее предложение."
#
# # Инициализация переменной с результатом
# result = "не найден"
#
# # Цикл произведет единственную итерацию
# # в случае наличия в тексте pythonru и
# # не сделает ни одной, если таких слов нет
# for j in get_pythonru(text):
#     result = "найден"
#     break
#
# print (f'Результат поиска: {result}')
#

#task1
# Напишите функцию sum_range(start, end), которая суммирует все целые
# числа от значения «start» до величины «end» включительно. Если
# пользователь задаст первое число большее чем второе, просто поменяйте
# их местами.

# "zadacha1"
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     s = 0
#     for i in range(start, end+1):
#         s += i
#     return s
# a, b = map(int, input("napiwite dva chisla: ").split())
# print(sum_range(a, b))


#task2
# def ari(a, b, operation):
#     if operation == "+":
#         print(f"{a} + {b} = {a + b}")
#     elif operation == "-":
#         print(f"{a} - {b} = {a - b}")
#     elif operation == "*":
#         print(f"{a} * {b} = {a * b}")
#     elif operation == "/":
#         if b != 0:
#             print(f"{a} / {b} = {a / b}")
#         else:
#             print('ZeroDivisionError')
#     else:
#         print("не известная операция")
#
#
# a = int(input("Введите 1 число: "))
# b = input("Введите операцию: ")
# c = int(input("Введите 2 число: "))
# ari(a, c, b)


#task3

# def func(*listok):
#     c = sum(listok)
#     return c
#
#
# a = func(1, 2, 3, 4, 5)
# print(a)


# task4
# Напишите функцию, которая принимает длину и ширину
# четырехугольника. Четырехугольник может быть прямоугольным или
# квадратным. Если это квадрат, необходимо вернуть его площадь. Если это
# прямоугольник, вернуть его периметр


# a = int(input('A: '))
# b = int(input('B: '))
#
# def func(integer1, integer2):
#     if a == b:
#         print(f'Square = {a * b}')
#     elif a != b:
#         print(f'Perimeter = {(a + b) * 2}')
#
# func(a, b) # передать переменые в функции




#task5
# lst1 = ["tail", "body", "head"]
#  def save(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
# sv = save(lst1)
# print(sv)







