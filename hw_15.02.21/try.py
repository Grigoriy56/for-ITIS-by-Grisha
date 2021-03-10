from double import del_d
from spl import *
from number import *
from twins import *
from russians import *

'''Это тестовый файл для функций. Тест делаю на db1'''

with open ('db1', 'r', encoding='KOI8-U') as f:
    book = f.read()

book = [i for i in book.split('\n')]
book = del_d(book)
book = spl(book)

book = wrong_number(book)
book = plus(book)


book = del_s(book)
book = add_s(book)
for i in book:
    print(i)
#rus = find(book)



#print(rus)
#print(rus)

#ip_twins = ip(book)
#print(ip_twins)
#for i in book:
    #print(i)