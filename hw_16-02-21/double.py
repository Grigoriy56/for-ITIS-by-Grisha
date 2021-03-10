def del_d(list):
    for str in list:
        if list.count(str) > 1:
            while list.count(str) != 1:
                list.remove(str)
    return list
