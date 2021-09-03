import numpy.random
import random


def generate(n, m, ran=False):
    if ran:
        return [[random.randint(0, 100) for i in range(n)] for j in range(m)]
    return [[0 for i in range(n)] for j in range(m)]

def maxime(matrix, row=False, col=False):
    if row and col:
        None

    if row:
        s = 0
        for r in range(len(matrix)):
            s1 = 0
            for c in range(len(matrix[r])):
                s1 += matrix[r][c]
        if s1 > s:
            s = s1
            m_row = r
        return matrix[m_row]

    if col:
        s = 0
        for c in range(len(matrix[0])):
            s1 = 0
            for r in range(len(matrix)):
                s1 += matrix[r][c]
        if s1 > s:
            s = s1
            m_col = c
        fin = []
        for i in range(len(matrix)):
            fin.append(matrix[i][m_col])
        return fin
    if not col and not row:
        matrix_m = matrix[0][0]
        for r in matrix:
            for c in matrix[r]:
                if matrix[r][c] > matrix_m:
                    matrix_m = matrix[r][c]
        return matrix_m


def sub(matrix, r1, r2, c1, c2):
    array = []
    time = []
    for r in range(r1, r2+1):
        array.append(time)
        time = []
        for c in range(c1, c2+1):
            time.append(matrix[r][c])
    array.append(time)
    return array[1:]


def rotate(matrix, r1, r2, c1, c2):
    if r2 - r1 != c2 - c1:
        return "Ошибочка вышла"

    def transpose(matrix, r1, r2, c1, c2):
        slice_m = sub(matrix, r1, r2, c1, c2)
        for r in range(len(slice_m)):
            for c in range(r, len(slice_m)):
                x = slice_m[r][c]
                slice_m[r][c] = slice_m[c][r]
                slice_m[c][r] = x
        return slice_m
    r_slice = transpose(matrix, r1, r2, c1, c2)
    print(*r_slice, sep='\n')
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            x = r - r1
            y = c - c1
            matrix[r][c] = r_slice[x][y]
    return matrix



