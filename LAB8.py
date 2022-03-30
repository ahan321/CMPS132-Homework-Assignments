# This function performs vector addition and subtraction. does so by checking the operation value of the function, and
# then utilizing a single-line for loop in order to iterate through both dimensions of the matrix.
def matrixCalculator(matrix1, matrix2, operation):
    if operation == "add":
        return [[matrix1[j][i] + matrix2[j][i] for i in range(len(matrix1[0]))] for j in range(len(matrix1))]
    if operation == "sub":
        return [[matrix1[j][i] - matrix2[j][i] for i in range(len(matrix1[0]))] for j in range(len(matrix1))]


'''This function finds digits in the number that satisfies the conditions in the fn parameter, and then multiplies them.
Modulo arithmetic is utilized to iterate through each digit.'''
def mulDigits(num, fn):
    product = 1
    while num > 0:
        digit = num % 10
        if fn(digit):
            product *= digit
        num = num // 10
    return product


'''This function finds the count of a perticular value in a number.  This function utilizes nested functions, whereby
the outer function takes in the number to be found while the inner function takes in the number to be searched through.'''
def getCount(x):
    def frequency(n):
        sum = 0
        if n < 0:
            n *= -1
        while n > 0:
            digit = n % 10
            if x == digit:
                sum += 1
            n = n // 10
        return sum
    return frequency


'''This function iterates through an iterable object, returning a tuple which shows the index number and the value in that
index.'''
def itemize(seq):
    count = 0

    while count < len(seq):
        yield count, seq[count]
        count += 1


'''This function creates a range function that works with floats.  It begins by first determining the number of arguments
inserted by the user, and then determining whether the sequence is upwards or downwards. After this, a simple while loop
is used to iterate through the values.'''
def frange(*args):
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')

    if start > stop:
        current = start
        while current > stop:
            yield round(current, 3)
            current += step
    elif stop > start:
        current = start
        while current < stop:
            yield round(current, 3)
            current += step


'''This function generates a fibbonaci sequence that also satisfies a specific condition (given by the fn parameter).'''
def genFib(fn):
    a = 0
    b = 1
    if fn(0):
        yield 0
    if fn(1):
        yield 1
    while True:
        c = a + b
        if fn(c):
            yield c
        a = b
        b = c

    