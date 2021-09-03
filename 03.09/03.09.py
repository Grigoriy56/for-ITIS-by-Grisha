import re
import pickle

with open('surnames.pickle', 'rb') as file:
    file = pickle.load(file)
    file = ' '.join(file)


file = re.findall(r'[АЁЯЮЕОУЭЫИ].*[^аоуюёяеыэ]$', file)

print(2)