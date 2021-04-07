a='+79824075208'
for i in range(len(a)):
    x = ''
    for j in a[-1:-8:-1]:
        x += j

    x += ' '
    print(x)
    for j in a[-8:-11:-1]:
        x += j
    x += ' '
    print(x)
    for j in a[-11:-len(a)-1:-1]:
        x += j
    x += ' '
    print(x)
