import re
import pickle

with open('surnames.pickle', 'rb') as file:
    file = pickle.load(file)

sur_names = []
for e in file:
    j = re.findall(r'[АОУЫЭИЁУЮ][а-я]*-?[а-яА-Я]*[^аоуэыиюеёАОУЫЭИЁУЮьъЬЪ]\b', e)
    if e == ''.join(j):
        sur_names.append(e)
pдrint(3)ж