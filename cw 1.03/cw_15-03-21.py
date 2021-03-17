
def mysum(*args):
    return sum(args)


def f2(array, a=False, b=1):
    for i in range(len(array)):
        array[i] = array[i] * b

    if a:
        proiz = 1
        for i in array:
            proiz *= i
        return proiz
    else:
        return sum(array)


arr = [1,2,4,5,5,6]


def test3(array, **kwargs):
    for k in kwargs:
        if k == 'mul':
            mul = kwargs['mul']
            array = [elem * mul for elem in array]
        if k == 'sub':
            sub = kwargs['sub']
            array = [elem - sub for elem in array]
        if k =='div':
            div = kwargs['div']
            array = [elem / div for elem in array]
        if k == 'summ':
            summ = kwargs['summ']
            array = [elem + summ for elem in array]

    return array


print(test3(arr, sub=5, mul=3, div=2))
