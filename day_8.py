# встроеные функции . ошибки .исключения

# а = - (1)
# b = 1
# print(a) #

#a = 'qwerty'
#print(all(a)) # если все объекты верны он возрашяет try

#a = 1234
#print(any(a))#проверяет на хотябы 1 правельный обьект

#a = 'python'
#b = 'best'
# print(eval('25 + 3'))
# divmod(25, 3) | 25 // 3 | 25 % 3
# print('%s is the %s' %(a, b))
# print('{} is the {}'.format(a, b))
# print(f'{a} is the {b}


# Функция filter() в Python применяет другую функцию
# к заданному итерируемому объекту
# (список, строка, словарь и так далее), проверяя,
# нужно ли сохранить конкретный элемент или нет.
#  Простыми словами, она отфильтровывает то,
#  что не проходит и возвращает все остальное.


# a = [i for i in range(1, 11)]
# b = filter(lambda x: x % 2 == 0, a)
# # f = list(b)
# # print(f)
# for i in b:
#     print(i)


# city = ('Bishkek', "Osh", "Batken", "Kara-Balta")
# # b = filter(str.isalpha, city)
# b = filter(lambda x: len(x) % 2 ==0,filter(str.isalpha, city))
# print(list(b))

#1.
#Напишите скрипт, в котором вы намеренно вызываете исключения. Обработайте их.
#Посмотрите как они работают и сделайте выводы.

# a = 9
# b = 8
#
# try:
#     if a > b:
#         print(a / 0)
#
# except NameError:
#     print('Error')
# except ZeroDivisionError:
#     raise ZeroDivisionError('ZeroDivisionError: division by zerO')
# else:
#      print('Hello world')

#2
# Напищите скрипт, который запрашивает число у пользователя. Если это число будет
# больше 1000, то вызовите ошибку ValueError. В случае если число меньше нуля
# вызовите другую ошибку ValueError, но уже с вашим собственным описанием. Иначе
# просто выводите число.

#
# a = int(input("print num"))
# try:
#     if a > 1000:
#         raise ValueError("ValueError") # вызывает ошибку
#     elif a < 0:
#         raise ValueError("Еrror")
# except NameError:
#     print("hello")
# else:
#     print("введите число")
#



#4 Вам даны строки. Вычислить, являются ли они полиндромами.
# 'Aziza'
# 'racecar'
# 'noon',
# 'nO0n',
# 'slaves',
# 'kka;lsfkas;lf'
# 'poipoipoipoi'
# 'lllkkkjjjjjjkkkll'
# d = input('Enter print')
# if d != d[::-1]:
#
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#a = list(input())   # list() принимает любую итерацию (объект, который можно перебирать) в качестве параметра и возвращает список.
#print(dir(a))     # dir()при вызове без аргумента, возвращает список переменных, доступных в локальной области.
                   # Если передать функции объект, она вернет список атрибутов указанного объекта.
