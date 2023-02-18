# import random - встроеные модули
import string

# import tkinter - устоновленые модули


# import day_10 as gh
#  #from  day_10 import names - ваши модули
# print(gh.names)


#import dir.day_10 as fh
#print(string.ascii_uppercase)  #ABC

# import datetime
# date1 = datetime.date(2023,2,14)
# print(date1)

# import datetime
# date1 = datetime.datetime.now()
# print(date1)
# from datetime import datetime, date, time
# start = datetime.now()
# print(start)
# print(datetime.now() - start)
from datetime import datetime, date, time

# start = datetime.now()
# s = [i for i in range(1000000)]
# print(datetime.now() - start)

# start = datetime.now()
# d =[]
# for i in range (1000000)
#      d.append(i)
# print(datetime.now() - start)

# import os
# d = os.getcwd()
# print(d)


# import os
# directory = 'my derictory'
# os.mkdir(directory

# import os
# directory ='my derictory'
# parent_dir = '/Users/ikramsvarov/Desktop'
# path = os.path.join(parent_dir, directory) # создать папку на рабочем столе
#
# os.chdir(path)

import shutil
parent_dir = 'Users/ikramsvarov/Desktop'
file = 'text.txt.py'
shutil.copyfile('Users/ikramsvarov/Desktop', file)








