def find(list):
    for i in range(len(list)):
        list_r = []
        if list[i][2][0] == '8' or (list[i][2][0] == '+' and list[i][2][1] == '7'):
            list_r.append(list[i])
            #print(list_r)
    return list_r
#если через принт в функции, то выводит все, а если присваивать переменной функцию, то почему-то не все