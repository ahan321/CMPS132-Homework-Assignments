# This function reaches base case by slicing the list until only one element remains.  Once it reaches base case,
# it checks whether it contains the item.  If not, the recursive return statements are called where the first term of
# the list is checked for a match with item.  Once the recursion is complete, the total count of the item is returned.
def get_count(aList, item):
    if len(aList) == 1:
        if item in aList:
            return 1
        else:
            return 0
    else:
        if aList[0] == item:
            return 1 + get_count(aList[1:], item)
        else:
            return get_count(aList[1:], item)


# This function reaches the base case through slicing until only one element remains.  This function works in a similar
# manner to the previous function, except this function replaces items in a list.  While recursively returning values,
# the function checks the first element of the list and does all operations on it.
def replace(numList, old, new):
    if len(numList) == 1:
        if old in numList:
            return [new]
        else:
            return [numList[0]]
    else:
        if numList[0] == old:
            return [new] + replace(numList[1:], old, new)
        else:
            return [numList[0]] + replace(numList[1:], old, new)


# This function flattens the given list.  It does so by utilizing different levels of recursion.  The base case is
# reached when only one element remains in the list, and this is reached through slicing.  If any additional sub-lists
# are encountered, the same method is then applied on that list.  In a sense, two different processes of recursion
# are occurring at the same once the base case is reached, each return statement is executed recursively and a list is
# built out.
def flat(aList):
    if len(aList) == 1:
        if type(aList[0]) == list:
            if len(aList[0]) == 0:
                return []
            temp = aList[0]
            return flat(temp)
        else:
            return [aList[0]]
    else:
        if type(aList) == list and aList[0] == []:
            return flat(aList[1:])
        if type(aList) == list and type(aList[0]) == list:
            temp = aList[0]
            return flat(temp) + flat(aList[1:])
        elif type(aList) == int:
            return aList
        else:
            return [aList[0]] + flat(aList[1:])


# This is a relatively simple recursive function.  The base case occurs when n is below 10, and this is achieved through
# integer division and modulus.  After this, algebraic rules are used to then piece together each digit, leaving behind
# any repeated ones.
def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    if n < 10:
        return n
    else:
        temp = n % 10
        if temp == (n // 10) % 10:
            return neighbor(n // 10)
        else:
            return 10 * neighbor(n // 10) + temp
