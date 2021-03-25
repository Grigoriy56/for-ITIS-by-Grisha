with open('Война_и_мир.txt', 'r', encoding='utf-8') as file:
    book = file.read()


def task1(text):
    return text.replace('Анна Павловна', 'Anna Pavlovna')


def task2(text):
    return text.find('Princesse, ma parole')


def task3(text):
    return text.split()


def task4(lst):
    return len(lst)


def task6(lst):
    def rus(w):
        try:
            if 1072 <= ord(w[0]) <= 1103:
                return True
            else:
                return False
        except IndexError:
            return None

    lst = list(map(lambda s: s.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
            .replace(';', '').replace(':', '').replace('–', '').replace(')', '').replace('(', '')
            .replace('-', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '')
            .replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '')
            .replace('9', '').replace('&', '').replace('#', ''), lst))
    lst = list(filter(lambda x: rus(x), lst))
    return lst


def better_task6(lst):
    alph = [chr(i) for i in range(1072, 1104)]
    alph.append(' ')
    s_lst = ' '.join(lst)
    for i in lst:
        if i not in alph:
            s_lst.replace(i, '')
    # в некоторых словах остаётся это скобка по непонятным мне причинам. Даже отдельно она не убирается реплейсем
    s_lst.replace(']', '')
    return s_lst.split(' ')


def task7(lst):
    lst = len(''.join(lst)) / len(lst)
    return round(lst, 4)


def task8(lst):
    lst = list(map(lambda x: len(x), lst))
    return sum(lst)


def task9(lst):
    time = set(lst)
    final = dict()
    fin_final = []
    for i in time:
        final[i] = lst.count(i)
    final = [(k, final[k]) for k in sorted(final, key=final.get, reverse=True)]

    for k, v in final:
        fin_final.append((k, v))
        if len(fin_final) == 10:
            break
    return fin_final


def task10(lst):
    # когда я придумал, как написать alph, мне стало очень грустно. Я максмально не хотел копипастить в 6 задании,
    # переписвая алфавит, и в итоге накопипастил с replace...
    lst = ''.join(lst)
    alph = [chr(i) for i in range(1072, 1104)]
    num_alph = dict()
    final = []
    for i in alph:
        num_alph[i] = lst.count(i)
    num_alph = [(k, num_alph[k]) for k in sorted(num_alph, key=num_alph.get, reverse=True)]
    for k, v in num_alph:
        final.append((k, v))
        if len(final) == 10:
            break
    return final

# здесь по порядку с первого таска
book = task1(book)
franch = task2(book)
book = task3(book)
number = task4(book)
book = list(map(str.lower, book))# task5
#book = task6(book)
book = better_task6(book)
# t7 = task7(book)
# t8 = task8(book)
# t9 = task9(book)
# t10 = task10(book)
print(book)

