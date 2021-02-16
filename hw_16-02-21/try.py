from double import del_d
from spl import *
from number import *
from twins import *

'''Это тестовый файл для функций. Тест делаю на db1'''

with open ('db1', 'r', encoding='KOI8-U') as f:
    book = f.read()

book = [i for i in book.split('\n')]
book = del_d(book)
book = spl(book)
for i in book:
    print(i)
book = wrong_number(book)



ip_twins = ip(book)
print(ip_twins)
#for i in book:
    #print(i)