# def rec(x): # рекурсия, как вызвать функцию
#     print(x)
#     rec(x+1)
# rec(1)


# def rec(x):
#     if x > - 15:
#         print(x)
#         rec(x-1)
# rec(1)



# digit = int(input('Add digit: '))
# factorial = 1
# for i in range(1, digit+1):
#     factorial = factorial * i
#
# print(f"Factorial: {factorial}")



# digit = int(input('Add digit: '))
# def factorial(difit):
#     if difit == 1:
#         return digit
#     else:
#         return digit * factorial(digit-1)
#
# print(f"factorial: {factorial}")




# start = time.time()
# digit = 10   #int(input('Add digit: '))
# def factorial(digit):
#     if digit == 1:
#         return digit
#     else:
#         return digit * factorial(digit-1)
#
# print(f"Factorial: {factorial(digit)}")
# end = time.time()
# print(end - start)


# D = {
#     'Desktop:': ['rec.py', 'func.py', 'lesson45.py'],
#     'PycharmProjects:': {
#         'Day1:': ['lesson1.py', 'lesson2.py'],
#         "Day2:": ['lesson1.py', 'lesson2.py'],
#         "Day3:": ['lesson1.py', 'lesson2.py']
#     },
#     'Books:': ['Python_for_kids.pdf', 'Python_for_beginner.pdf']
# }
#
#
# def get_files(path, depth=0):
#     for f in path:
#         print(' '*depth, f)
#         if type(path[f]) == dict:
#             get_files(path[f], depth+1)
#         else:
#             print(" " * (depth+1), ' '.join(path[f]))
#
# get_files(D)




# def decor(function):
#     def wrapper(*args):
#         print('Start')
#         function()
#         print('End')
#     return wrapper
#
#
# @decor
# def hello():
#     print('Hello!')
#
#
# hello()



# names = {
#     1: 'Erkeen',
#     2: 'Edil',
#     3: 'Askar',
#     4: 'Cholponai',
#     5: 'Ikram',
#     6: 'Aleksey',
#     7: 'Evgeniy'
# }
#
# def decorator(function):
#     def wrapper(*args, **kwargs):
#         print('Before')
#         print(names)
#         function(*args, *kwargs)
#         print('After')
#         return function(*args, *kwargs)
#     return wrapper
#
#
# @decorator
# def change_name(names, id, name):
#     names[id] = name
#     return names
#
#
# print(change_name(names, 1, 'Erkin'))
# # print(names)



# def what_is(thing):
#     if thing is None:
#         print(thing, 'is None')
#     elif thing:
#         print(thing, 'is True')
#     else:
#         print(thing, 'is False')
#
# what_is(None)
# what_is(True)
# what_is(False)
# what_is(0)
# what_is([])
# what_is([0])
# what_is(0.0)
# what_is([0.0])








#task1

# def is_palindrome(s):
#     if len(s) < 1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False
# a = str(input("Введите строку:"))
# if (is_palindrome(a) == True):
#     print("Данная строка палиндром!")
# else:
#     print("Данная строка не палиндром!")


#task2
# digit = int(input('Add digit: '))
# factorial = 1
# for i in range(1, digit+1):
#     factorial = factorial * i
#
# print(f"Factorial: {factorial}")


#task3
#Напишите функцию lambda, которая вычисляет нам площадь прямоугольника по длинам двух его сторон(длина, ширина).

# l = int(input("введите длину "))
# s = int(input("введите ширину "))
# a = ((lambda x, y: x * y) (l, s))
# print(a)



#task4
# l = int(input())
# s = int(input())
# a = (lambda a, b: a if a>b else b)(l,s)
# print(a)


#task6
# import time
#
# def decor(func):
#     def wrapper(*args):
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start)
#     return wrapper
#
#
# @decor
# def ff():
#     print('!!!!!')
#
# ff()
#




