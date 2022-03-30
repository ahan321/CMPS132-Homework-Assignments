# The function runs a check on whether the input is a list, then checks whether each item is a number (float, integer),
# before squaring it and adding it to the sum.  The final tabulated sum is then returned.
def sumSquares(aList):
    if type(aList) == list:
        sum = 0
        for num in aList:
            if type(num) == float or type(num) == int:
                if num > 5 and num < 500:
                    sum += num ** 2
        return sum
    return