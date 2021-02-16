def wrong_number(list):
    for i in range(len(list)):
         list[i][2] = list[i][2].replace('(', '').replace(')', '').replace('-', '').replace('(', '')
         x = list[i][2]
         #if x[-8:-7] != ' ':
          #  x = x.replace(x[-8:-7], ' ' + x[-8:-7])
           # list[i][2] = x
    return list

#так как строка - незменяемые вид, я не знаю, как разбить по пробелу. не могу выполнить второй пункт.

