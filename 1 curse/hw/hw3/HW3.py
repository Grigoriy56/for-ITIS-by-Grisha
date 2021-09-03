from matplotlib import pyplot as plt
from math import sqrt
import datetime
def distance(x1, y1, x2, y2):
	"""
	Расчет расстояния между двумя точками
	Args:
		x1 y1 : Координаты 1-ой точки
		x2 y2 : Координаты 2-ой точки
	Returns:
		float: расстояние между ними
	"""

	dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	return dist

def read_data(path):
	"""
	Чтение файла и сохранение в словаре вида: ключ адрес, значения это кортеж (координата Х, коордианата Y, площадь)
	Пример: {'пр-кт Фатыха Амирхана д 91Б': (5.73063, 11.8712, 2095.0), ... }
	Args:
		path (str): путь к файлу
	Returns:
		dict: ключ адрес, значение (x, y, площадь)
	"""
	data = {}
	with open(path, 'r', encoding='utf-8') as file:
		book = file.read()
		book = book.split('\n')
		book = book[:len(book) - 1:]
		book = [i.split('\t') for i in book]
		for i in range(len(book)):
			data[book[i][0]] = float(book[i][1]), float(book[i][2]), float(book[i][3])
	return data

def reverse_dict(dict):
	"""
	Я не починил свою ide, чтобы одной командой разворачивать словарь, и написал для этого функцию ;)
	"""
	items = list(dict.items())
	n_dict = {k: v for k, v in reversed(items)}
	return n_dict

def the_best(database):
	"""
	Как task1, только возвращащет весь список лучший от лучшего к худшему
	"""
	radius = {}
	for house in database:
		radius[house] = 0
		for others in database:
			if distance(database[house][0], database[house][1], database[others][0], database[others][1]) <= 0.5:
				radius[house] += 1

	sort_key = sorted(radius, key=radius.get)
	sort_key = sort_key[::-1]

	return sort_key

def task1(database):
	"""
	Задача 1
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		помимо database могут быть любые другие аргументы
	Returns:
		list: координаты дома (x, y)
	"""
	t1 = datetime.datetime.now()
	radius = {}
	for house in database:
		radius[house] = 0
		for others in database:
			if distance(database[house][0], database[house][1], database[others][0], database[others][1]) <= 0.5:
				radius[house] += 1

	sort_key = sorted(radius, key=radius.get)
	k = sort_key[-1]
	ret = [(database[k][0], database[k][1])]
	t2 = datetime.datetime.now()
	print(t2-t1)
	return ret


def task2(database):
	"""
	Задача 2
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		помимо database могут быть любые другие аргументы
	Returns:
		list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
	"""
	t1 = datetime.datetime.now()
	b_list = the_best(database)
	bad = []
	good = []
	while len(good) < 15:
		for i in b_list:
			if i not in bad:
				good.append((database[i][0:2]))
			for shop in database:
				if distance(database[i][0], database[i][1], database[shop][0], database[shop][1]) <= 1:
					bad.append(shop)
	t2 = datetime.datetime.now()
	print(t2-t1)
	return good[:10]


def task3(database):
	"""
	Задача 3
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		помимо database могут быть любые другие аргументы
	Returns:
		list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
	"""
	t1 = datetime.datetime.now()
	fin = []
	b_list = []
	square = {}
	for house in database:
		square[house] = 0
		for others in database:
			if distance(database[house][0], database[house][1], database[others][0], database[others][1]) <= 0.5:
				square[house] += 0.7 * database[others][2] / 18
	sort_key = sorted(square, key=square.get)
	sort_key = sort_key[::-1]
	for i in range(len(sort_key)):
		home = sort_key[i]
		for j in range(len(fin)):
			if distance(database[home][0], database[home][1], fin[j][0], fin[j][1]) <= 1:
				b_list.append(sort_key[i])
		if sort_key[i] not in b_list:
			fin.append((database[home][0], database[home][1]))
		if len(fin) > 14:
			break
	t2 = datetime.datetime.now()
	print(t2-t1)
	return fin[:15]


def plot(database, best_coords):
	"""
	НЕ МЕНЯТЬ КОД!
	Отрисовка точек 2D
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		best_coords (list): для задачи 1 это (x, y), для задачи 2-3 это [(x1,y1), (x2,y2) ... (xn,yn)]
	"""
	plt.close()
	fig, ax = plt.subplots(figsize=(8, 8))
	plt.plot([coord[0] for coord in database.values()],
	         [coord[1] for coord in database.values()], '.', ms=5, color='k', alpha=0.5)
	if isinstance(best_coords[0], tuple):
		for x, y in best_coords:
			circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
			ax.add_patch(circle)
		plt.plot([coord[0] for coord in best_coords],
		         [coord[1] for coord in best_coords], '.', ms=15, color='r')
	elif isinstance(best_coords[0], float):
		x, y = best_coords
		circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
		ax.add_patch(circle)
		plt.plot(*best_coords, '.', ms=15, color='r')
	else:
		raise ValueError("Проверь, что подаёшь список кортежей или кортеж из двух координат")
	plt.show()

def homework():
	# path = "/home/alex/buildings"
	path = "buildings"
	database = read_data(path)

	# best_task1 = task1(database)
	# plot(database, best_task1)

	best_task2 = task2(database)
	plot(database, best_task2)

	# best_task3 = task3(database)
	# plot(database, best_task3)

if __name__ == '__main__':
	homework()

