def reverse(aList):
    for i in range(len(aList) - 1, -1, -1):
        print(aList)
        aList.append(aList[i])
        aList.pop(i)
    return aList


def onlyTwo(n):
    counter = 0
    while n > 0:
        rem = n % 10
        if rem == 2:
            counter += 1
        n = n // 10
    return counter


def minmax(data):
    min = data[0]
    max = data[0]
    for i in data:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)

def foo(x):
    return x


def bar(x,y):
    if x(y):
        return not y
    return y
x = 3
x = bar(foo,x)
foo = bar(foo,0)
total = foo(7)
d