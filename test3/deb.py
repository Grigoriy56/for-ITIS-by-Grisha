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