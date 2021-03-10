def spl(list):
    list = [[i] for i in list]
    for i in range(len(list)):
        list[i] = list[i][0].split("\t")
    return list

