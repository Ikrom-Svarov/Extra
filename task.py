#task1
#a = (['n', 'o', 'h', 't', 'y', 'p', ' ', ',', 'u', 'o', 'y', ' ', 'e', 'v', 'o', 'l', ' ', 'i'])
#a.reverse()
#print(a)
#task2
"""
s = ['Am', 'I', 'a', 'good', 'programmer', '?']
s[1] = "w"
s[5] = "!"
print(s)
s.pop(5)
print(s)
"""
#task3
"""
a = [45527, 54545, 232324, 372842487, 5545454]
a.sort()
print(a[-1]/len(a))
"""

#task4
"""
4
а = int(input("введите число до 5"))
b = ['hehdk', 'jsjidi','jedudi','jdjinej',2133]
s = []
for i in range(a):
    s.append(b[i])
    print(s)
"""
"""
a = int(input("Введите число до 6: "))
b =  ["dfdfdffd", "dfdfdfd", "gdfgdg", "dfdfdf", 1324, 'bgbd']

c = []
for element in range(a): # range(3) --> (0, 1, 2)
    c.append(b[element])
print(tuple(c))"""
#task5
#5. У вас есть список из строк. Ваша задача найти самую длинную, затем привести каждую остальную
#строку к такой же длине заполняя их символом "_".

"""
s = ['Something', 'in', 'the', 'way',
     'mmmmmmm', 'btw', 'python', 'is',
     'better', 'than', 'js']
smax = max(s, key=len)
for i in range(len(s)):
    while len(s[i]) < len(smax):
        s[i] += '_'
print(s)
"""

