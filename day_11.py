#функции
# def square(integer):
#     s = integer ** 2
#     return s
#
# print(square(10))
from typing import Union, Any

# f = [1,3,4]
# def square(integer):
#     global f
#     f = ['df',34]
#     return integer ** 2
#
# square(10)
# print(f)



# def hello():
#     return "Hello world"
# def append():
#     s = hello()
#     return s + '!!!'
# print(append())


# def summ(integer,string):
#     return int(integer) * str(string)
# g = summ(string='astr',integer=10)
# print(g)


# name = input('your name:')
# last_name = input("your last_name:")
# age = int(input("your age:"))
# def func(name, last_name, age):
#     if age < 25 :
#         return f f'привет {name} {last_name}, тебе {age}, молокосос'
#     elif age > 25 and age < 33:
#
#     q = func(name=jon,last_name=smith,age=23)


# name = input('Your name: ')
# last_name = input('Your last_name: ')
# age = int(input('Your age: '))


# def func(name, last_name, age):
#     if age < 25:
#         return f'Привет {name} {last_name}, тебе {age} молокосос!'
#     elif age > 25 and age < 33:
#         return f'Привет {name} {last_name}, тебе {age} машина!'
#     else:
#         return f'Привет {name} {last_name}, тебе {age} дед!'
#
#
# q = func(name=name, last_name=last_name, age=age)
# print(q)


# def func(name, last_name, age):
#     if age < 25:
#         return f'Привет {name} {last_name}, тебе {age} молокосос!'
#     elif age > 25 and age < 33:
#         return f'Привет {name} {last_name}, тебе {age} машина!'
#     else:
#         return f'Привет {name} {last_name}, тебе {age} дед!'
# if age > 18 :
#     print(func(name=name, last_name=last_name, age=age))
# else :
#     print('forbidden')
#
#
#
# q = func(name=name, last_name=last_name, age=age)
# print(q)
#task1
# name = input('Your name: ')
# last_name = input('Your last_name: ')
# def func(first_name, last_name):
#     return f'Привет {first_name.capitalize()} {last_name.capitalize()}'
#
# d = func(name,last_name)
# print(d)


#task2
# Напишите функцию, которая принимает в себя строку и в случае, если вся строка состоит из уникальных символов,
# верните True, иначе False.

# def func(str):
#     d = set(str) # set чтобы разобрать переменую
#     if len(str) == len(d):
#         return True
#     else:
#         return False
#
# word = input('введите слово: ')
# print(func(word))

#task3
# Создайте функцию, которая примет в себя такие аргументы: Имя покемона, его уровень в виде числа и его тип.
# Покемон считается слабым, если его уровень меньше или равен 20, средним если его уровень выше 20 и меньше или равен
# 50. Если его уровень выше 50, то покемон считается сильным.
# Покемон может быть огненного, водяного и землянного типов.
# Функция должна возвращать строку в таком виде: "{Имя покемона}, {слабый/средний/сильный (в зависимости от уровня)}
# покемон {тип покемона} типа."

# name = input('имя покемона:')
# level = int(input('уровень: '))
# type_d = str(input("тип: "))
#
#
# def chek(name,lvl,type):
#     if lvl >=0 and lvl <= 20:
#         return f'{name}. слабый. {type}'
#
#     elif lvl <= 50 and lvl >= 21:
#         return f'{name}. средний. {type}'
#
#     elif lvl > 50 :
#         return f'{name}. силный. {type}'
#     else:
#         return 'error'
#
#
# print(chek(name, level, type_d))

# task4
# Напишите функцию, которая принимает в себя произвольный список из чисел и возвращает кортеж, внутри которого
# хранится самое маленькое и самое большое число из списка.





#task5
# Создайте функцию, которая возвращает 'Hello world', затем создайте вторую функцию, которая принимает ее как аргумент
# и добавляет к ней новую строку ' and Python!'.

# def hello():
#   return "Hello world"
# def append():
#     s = hello()
#     return s + ' and Python'
# print(append())