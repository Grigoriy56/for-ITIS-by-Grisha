a = ['PHP', 'PHP', 'Python', 'PHP',
'Python', 'JS', 'Python', 'Python',
'PHP', 'Python']

print(list((i, a.count(i)) for i in a if i == max(a, key=a.count))[0])