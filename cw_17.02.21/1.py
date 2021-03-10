a = [4,6,8,1,-9,0,1,2,1,7]

def f1(list, x, y):
    return sum(list[x:y+1])

#print(f1(a,2,4))


def f2(list, de):
    for i in range(list.count(de)):
        list.remove(de)
    return list


def f2n(list, de):
    f_list = []
    for i in list:
        if i != de:
            f_list.append(i)
    return f_list

def f3(list, start, end):
    return list[:start+1] + list[end:start-1:-1] + list[end+1:]

# print(f3(a, 2,5))
def f4(list, step):
    return list[-step::] + list[-len(list):-step:]
#print(f4(a, 2))

def f5(*args):
    list = []
    for i in args:
        list += i
    return list
# a = [1,2,3]
# b = [4,5]
# c = [6]
# print(f5(a, b, c))+

def f6(list1, list2):
    a = len(list1)
    b = len(list2)
    list3 = []
    if a <= b:
        for i in range(a):
            list3.append(list1[i])
            list3.append(list2[i])
        for i in range(b-a):
            list3.append(list2[0])

    else:
        for i in range(b):
            list3.append(list1[i])
            list3.append(list2[i])
        for i in range(a-b):
            list3.append(list1[0])

    return list3


#print(f6([1,1,1,1,1],[0,0,0,0,0]))


def f7(list1,list2):
    a = len(list1)
    b = len(list2)
    if a <= b:
        list3 = list(zip(list1,list2))
        list3 += list2[-1:a-b-1:-1]
    else:
        list3 = list(zip(list1, list2))
        list3 += list1[-1:b-a - 1:-1]
    return  list3

#print(f7([1,1,1,1,1,1,1],[0,0,0,0,0]))

def f8(list1):
    list2 = []
    for i in range(0 ,len(list1) - 1, 2):
        list2.append((list1[i], list1[i+1]))
    return list2
a = [1,2,3,4,5,6]
#print(f8(a))