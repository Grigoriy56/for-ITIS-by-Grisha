a = [0,4,6,8,1,-9,0,1,2,1,7,0]
b = [1,4,3,1,1]
с = [4,1,1,1,3]


def f9(a):
    return len(a) == 0


def f10(a):
    return a[::2]


def f11(x, y):
    x.sort()
    y.sort()
    return x == y


def f12(a, b):
    a = (*a, *b)
    return a


def f13(a, d):
    cort = tuple(i for i in a if i >= d)
    lst = [j for j in a if j < d]
    return cort, lst


# print(*f13(a, 4))


def f14(a):
    return a == a[::-1]


def f15(a):
    return [i for i in range(len(a)) if a[i] != 0]


def f16(arr, num):
    arr = sorted(arr)
    for i in range(0 , -len(arr)-1, -1):
        check1, check2 = arr[i], arr[i-1]
        if abs(num - check1) <= abs(num - check2):
            return check1


# print(f16(a, 3))


def f17(arr):
    new = sum(arr[:3:])
    x = 0
    for i in range(1, len(arr)-3):
        comp = sum(arr[i:i+3:])
        if comp > new:
            new = comp
            x = i
    return arr[x:x+3]


#print(f17(a))


def f18(arr):
    leng = len(arr)
    centr = leng / 2
    if leng % 2 == 0:
        centr = int(centr)
        del arr[centr]
        del arr[centr - 1]
    else:
        centr = int(centr + 0.5)
        del arr[centr]
    return arr

print(f18(a))
