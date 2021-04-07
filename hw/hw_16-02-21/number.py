def wrong_number(list):
    for i in range(len(list)):
         list[i][2] = list[i][2].replace('(', '').replace(')', '').replace('-', '').replace('(', '')
         x = list[i][2]
         #if x[-8:-7] != ' ':
          #  x = x.replace(x[-8:-7], ' ' + x[-8:-7])
           # list[i][2] = x
    return list
#так как строка - незменяемые вид, я не знаю, как разбить по пробелу. не могу выполнить второй пункт.


#приведение к формату +7
def plus(list):
    for i in range(len(list)):
        if list[i][2][0] != '+' and list[i][2][0] != '8':
            x = '+'
            for j in list[i][2]:
                x += j
            list[i][2] = x
        elif list[i][2][0] == '8' and list[i][2][1] == '9':
            x = '+7'
            for j in list[i][2][1:]:
                x += j
            list[i][2] = x
        elif list[i][2][0] == '8' and list[i][2][1] != '9':
            x = '+'
            for j in list[i][2]:
                x += j
            list[i][2] = x
    return list


#разделяю номера на пробелы, сначала удалю все пробелы, чтобы было проще написать единую функцию(да, не оптимизировано)
def del_s(list):
    for i in range(len(list)):
        list[i][2] = list[i][2].replace(' ', '')
    return list


def add_s(list):
    for i in range(len(list)):
        x = ''
        for j in list[i][2][-1:-8:-1]:
            x += j
        x += ' '
        for j in list[i][2][-8:-11:-1]:
            x += j
        x += ' '
        for j in list[i][2][-11:-len(list[i][2])-1:-1]:
            x += j
        list[i][2] = x[-1:-len(x)-1:-1]
    return list