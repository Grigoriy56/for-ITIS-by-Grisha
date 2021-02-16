from double import del_d
from spl import *
from number import *
from twins import *

with open ('db2', 'r', encoding='KOI8-U') as f:
    book = f.read()

book = [i for i in book.split('\n')]
book = del_d(book)
book = spl(book)
book = wrong_number(book)

#это для поиска пользователей с одинаковым ip
ip_twins = ip(book)



