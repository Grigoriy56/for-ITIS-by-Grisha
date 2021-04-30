from bs4 import BeautifulSoup
import pickle

# with open('page.html', 'r', encoding='utf-8') as f:
#     page = f.read()
#     page = BeautifulSoup(page, 'lxml')

# all = page.find_all('div', class_="apartament")

# telephones = page.find_all("div", class_="mobile-number")
# telephones = [i.span.text for i in telephones]
# # pickle.dump(telephones, open('telephones.pickle', 'wb'))
#
# flats = page.find_all("h5", class_="apartament-title")
# flats = [i.text.split(',') for i in flats]
# for i in range(len(flats)):
#     flats[i].append(telephones[i])
# pickle.dump(flats, open('flats.pickle', 'wb'))

# with open('telephones.pickle', 'rb') as f:
#     numbers = pickle.load(f)

# I have used library pickle for economy my time

with open('flats.pickle', 'rb') as f:
    flats = pickle.load(f)


with open('8_ABC.csv', 'r', encoding='utf-8') as f:
    page = f.readlines()[1:]
    page = [i.split(';') for i in page if "Республика Татарстан" in i.split(';')[5]]
ultimate_tatar_numbers = {i[0]: tuple(tuple(j[1:3]) for j in page if j[0] == i[0]) for i in page}
del page

with open('9_ABC.csv', 'r', encoding='utf-8') as f:
    tatar = f.readlines()[1:]
    tatar = [i.split(';') for i in tatar if "Республика Татарстан" in i.split(';')[5]]
ultimate_tatar_numbers.update({i[0]: tuple(tuple(j[1:3]) for j in tatar if j[0] == i[0]) for i in tatar})
del tatar


def find_t(dict_x, list_x):
    # I had no idea, how do this with lambda
    finds = []
    for numb in list_x:
        if numb[3][4:7] in dict_x.keys():
            for interval in dict_x[numb[3][4:7]]:
                if int(interval[0]) <= int(numb[3][9:]) <= int(interval[1]):
                    finds.append(numb)
                    # print(interval[0], interval[1],  )
                    break
    return finds


def find_home(list_x):
    def finds(stra):
        num = ''
        for i in stra:
            if i == '/':
                return int(num)
            num += i

    fin = []
    for i in list_x:
        if i[0][0] == '3' and 45 <= float(i[1][1:6]) <= 65 and 3 <= finds(i[2]) <= 15:
            fin.append(i)
    return fin


flats = find_t(ultimate_tatar_numbers, flats)
flats = find_home(flats)

pickle.dump(flats, open('result.txt', 'wb'))
