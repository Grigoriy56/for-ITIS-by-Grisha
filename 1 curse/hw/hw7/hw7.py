data = (line.replace('\n', '') for line in open('dataset'))
data = (i.split(';') for i in data)
next(data)
data_filter = (i for i in data if i[7] == 'a')
all_raised = int(sum(int(i[6]) for i in data_filter))
# from this string data is died
print(weight_raised := all_raised / (30e6 - 10e6) * 1000)
data = (line.replace('\n', '') for line in open('dataset'))
data = (i.split(';') for i in data)
next(data)
data = (i for i in data if int(i[6]) < weight_raised and i[7] == 'a')

print(final := list(tuple((i[0], i[2], i[6]) for i in data)))
