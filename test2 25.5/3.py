a = 'Привет, Oleg! Это FBI!'
b = list(map(lambda x: x.lower() if x.isupper() else x.upper(), a))
print(''.join(b))

# мог в одну строку, но бонуса не подвезли :D
