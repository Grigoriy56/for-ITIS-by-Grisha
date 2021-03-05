mydict = {2:9, 5:-3, 3:12, 7:3, 4:20, 1:9, 6:9, 11:3, 13:6}
def fill(dict, N):
    list = []
    for k in dict:
        list.append(k)
    for i in range(1, N+1):
        if i not in list:
            dict[i] = '!!'
    return dict
print(fill(mydict, 14))

def summarize(N):
    x = str(N)
    y = 0
    while y > 10 or y == 0:
        y = 0
        for i in range(len(x)):
            y += int(x[i])
        x = str(y)
    return y
print(summarize(156))



mystr ='Привееет! Как Дела?'
def salt_lang(string):
   alph =  ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']
   list = []
   for i in string:
        list.append(i)
        if i in alph:
            list.append('с')
            list.append(i)
   s = ""
   for i in list:
        s += i
   return s
print(salt_lang(mystr))


mydict = {2:9, 5:-3, 3:3, 7:3, 4:20, 1:9, 6:9, 11:3, 13:6}


def no_dup(dict):
    s = set()
    dic = {}
    for v in dict.values():
        if v in s:
            dic = {key: value for key, value in dict.items() if value in set}
        s.add(v)
    return dic

print(no_dup(mydict))

#def set_merge(*args):

   # return set(*i for i in args)
#print(set_merge({1,2},{1,0,6,7},{10,0},{1,9,-3}))

