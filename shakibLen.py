def sakib_len(x):
    a = []
    a.extend(x)
    a.sort()
    for i in a:
        x = a.index(i)

    return x+1


print(sakib_len('1234'))
print(sakib_len('qwert'))
