from double import del_d
from spl import *
from number import *
from twins import *

with open ('db2', 'r', encoding='KOI8-U') as f:
    book = f.read()

#формирую список
book = [i for i in book.split('\n')]

#удаляю дубли
book = del_d(book)

#формирую списки в списке для уобной работы
book = spl(book)

#удаляю -,(,)
book = wrong_number(book)

#привожу всё к формату +xxxxxxxx
book = plus(book)

#удаляю пробелы в номерах, чтобы далее было проще привести
book = del_s(book)

#привожу к правильным пробелам
book = add_s(book)

#ищу русские номера и формирую отдельный список
rus = find(book)

#это для поиска пользователей с одинаковым ip
ip_twins = ip(book)

print(book)

