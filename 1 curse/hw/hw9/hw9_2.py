import textwrap
import datetime
from random import random
# для вызова потоков через Pool
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
import pickle
numbers = []
heads = []

with open('page.html', 'r', encoding="utf8") as f:
    f = f.read()
f = BeautifulSoup(f, 'lxml')


def head(array):
    for i in f.find_all('h5'):
        array.append(i.text)


def number(cont, array):
    for i in cont.find_all("div", attrs={"class": "mobile-number"}):
        array.append(i.text)

#
# t1 = Thread(target=head, args=(f, heads))
# t2 = Thread(target=number, args=(f, numbers))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

telephones = {}
headss = []


def find_tatar(array):
    base = ['8_ABC.csv', '9_ABC.csv']
    for i in range(2):
        with open(base[i], encoding="utf8") as f:
            f = f.readlines()
            f = [i.split(';')[0:3] for i in f[1:] if 'Татар' in i.split(';')[5]]

        for num in f:
            if num[0] in array.keys():
                array[num[0]].append(tuple(num[1:]))
            else:
                array[num[0]] = []
                array[num[0]].append(tuple(num[1:]))


def my_zip(x, y):
    for i in range(len(x)):
        temp = (*x[i].split(','), y[i])
        headss.append(temp)


# t1 = Thread(target=find_tatar, args=(telephones, ))
# t2 = Thread(target=my_zip, args=(headss, heads, numbers))
# t1.start()
# t2.start()
# t1.join()
# t2.join()





def final_sort():
    pool = ThreadPool(10)
    global answers
    answers = []




    def my_sort(value):
        number = ''
        floor = ''
        for symb in value[1]:
            if symb == 'м':
                break
            number += symb

        for symb in value[2]:
            if symb == '/':
                break
            floor += symb
        if value[0][0] == '3' and 35 <= float(number) <= 65 and 2 < int(floor) < 16:
            code = value[3][4:7]
            if code in telephones.keys():
                number = int(value[3][9:])
                for v in telephones[code]:
                    if int(v[0]) <= number <= int(v[1]):
                        answers.append(value)

    pool.map(number, heads)
    pool.map(head, headss)
    pool.map(find_tatar, telephones)
    pool.map(my_zip, heads, numbers)
    pool.map(my_sort, headss)


# answers = final_sort()


def final_final_sort():
    ti1 = datetime.datetime.now()

    # t1 = Thread(target=head, args=(f, heads))
    # t2 = Thread(target=number, args=(f, numbers))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    #
    # t1 = Thread(target=find_tatar, args=(telephones,))
    # t2 = Thread(target=my_zip, args=(headss, heads, numbers))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    final_sort()


    ti2 = datetime.datetime.now()
    print(ti2-ti1)


final_final_sort()
# pickle.dump(answers, open("result.txt", "wb"))