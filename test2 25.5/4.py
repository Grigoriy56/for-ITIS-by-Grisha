a = 'acbfbacffaabbccufacbbafaa'
b = ['a', 'b', 'c']
def long(word, alph):
    final = []
    for i in range(len(word)):
        st = ''
        for j in word:
            if j in alph:
                st += j
            if j not in alph:
                final.append(st)
                st = ''
                continue
    return max(*final, key=len)

print(long(a, b))
