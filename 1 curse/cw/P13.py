import pickle


# with open('freqrnc2011.csv', encoding='utf-8') as file:
#     file.readline()
#     book = [line.strip().split('\t')[:3] for line in file]
#     book = [i for i in book if i[1] == 's']
#     book.sort(key=lambda x: float(x[2]), reverse=True)
#     book = book[:15000]
#     book = [i for i in book if 4<len(i[0])<10]
#
#
# pickle.dump(book, open('dad.csv', 'wb'))

with open('dad.csv', encoding='utf-8') as file:
    book = file.read()