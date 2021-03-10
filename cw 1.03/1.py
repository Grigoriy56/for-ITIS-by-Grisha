rows = 5
cols = 7
matrix = [[row * cols + col + 1 for col in range(cols)] for row in range(rows)]
matrix[0] = [0] * cols
matrix[-1] = [0] * cols
for i in range (5):
    matrix[i][0] = 0
    matrix[i][-1] = 0

m = []
for i in range(rows):
    for j in range(cols):
        m.append(matrix[i][j])



n = []
n.append(matrix[::])
m[0] =999
print(m, n)
# row строка
def sub(m, r1, r2, c1, c2):
    new = []
    for i in



