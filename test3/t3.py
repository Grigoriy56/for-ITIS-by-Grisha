def split_pairs(st):
    if len(st)%2 == 0:
        fin = []
        for i in range(0, len(st)-1, 2):
            fin.append(st[i]+st[i+1])
    else:
        fin = []
        for i in range(0, len(st)-2, 2):
            fin.append(st[i]+st[i+1])
        fin.append(st[-1]+'_')
    return fin
print(split_pairs('abc'))


def max_triple(arr):
    fin = arr[-1:-4:-1]
    my_max = sum(arr[-1:-4:-1])
    for i in range(-1, -len(arr)-1, -1):
        temp = sum(arr[i:i-3:-1])
        if temp > my_max:
            my_max = temp
            fin = arr[i:i-3:-1]
    return fin

a = [2,4,6,1,-3,9,-4,3,9,4,0,1]
print(max_triple(a))


def check(st):
    if len(st) < 9:
        return False
    dig = 2
    symb = 2
    up = 2
    low = 2
    for i in st:
        if i.isalpha():
            if i.islower():
                low -= 1
            if i.isupper():
                up -= 1
        if i.isdigit():
            dig -= 1
        if not i.isdigit() and not i.isdigit():
            symb -= 1
    if dig < 1 and symb < 1 and up < 1 and low < 1:
        return True
    return False

print(check(' G1#!nbP0_123 '))


def merge(*args):
    fin = args[0] # на вывод
    my_keys = fin.keys()  #мои ключи
    length = len(args)
    for i in range(1, length):
        temp_keys = args[i].keys() #проверк
        for k in temp_keys:
            if k in my_keys:
                if type(fin[k]) is list:
                    temp = fin[k]
                else:
                    temp = [fin[k]]
                temp.append(args[i][k])
                fin[k] = temp
                my_keys = fin.keys()
            else:
                fin[k] = args[i][k]
    return fin

a = {1:2, 3:4}
b = {1:10, 2:5, 7:10}
c = {1:7, 2:10}
print(merge(a, b, c))
