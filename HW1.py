# HW1
# Due Date: 09/10/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


def rectangle(perimeter, area):

    # This function iterates through all possible lengths and widths in order to determine a suitable match.
    # It then returns the largest value between the length and the width of the rectangle.

    for l in range(1, perimeter):
        for w in range(1, perimeter):
            if l * w == area and 2 * l + 2 * w == perimeter:
                if l >= w:
                    return l
                elif l < w:
                    return w
    return False


def frequency(aString):

    # This function iterates through the string and determines if each value is in the alphabet.  If so, it adds to the
    # count of the character.  The iterated function also keeps track of the character with the largest count,
    # marking it as either a vowel or a consonant.  It then returns the result.

    aString = aString.lower()
    charCount = {}
    maxCount = 0
    type = ""

    for i in aString:
        if i.isalpha() == True:
            if i in charCount:
                charCount[i] = charCount[i] + 1
            else:
                charCount.update({f"{i}": 1})
            if charCount[i] > maxCount:
                maxCount = charCount[i]
                if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                    type = "vowel"
                else:
                    type = "consenant"
    return type, charCount


def successors(file):

    # This function start by reading the file, and then attempts to put a space between each symbol that lies within
    # the sentence in order to allow the split() function to catch it.  The function then splits the statement into a list,
    # and iterates on it, determining the next word and grouping them together using a dictionary using a for loop.  Lastly, the dictionary is returned.

    with open(file) as f:
        contents = f.read()

    if not contents.isalnum():
        i = 0
        while i < len(contents):
            if contents[i] == ",":
                left_half = contents[:i]
                right_half = contents[i+1:]
                replacement = " , "
                contents = left_half + replacement + right_half
                i += 2

            if contents[i] == ".":
                left_half = contents[:i]
                right_half = contents[i+1:]
                replacement = " . "
                contents = left_half + replacement + right_half
                i += 2
            i += 1

            if contents[i] == "?":
                left_half = contents[:i]
                right_half = contents[i+1:]
                replacement = " ? "
                contents = left_half + replacement + right_half
                i += 2
            i += 1

            if contents[i] == "!":
                left_half = contents[:i]
                right_half = contents[i+1:]
                replacement = " ! "
                contents = left_half + replacement + right_half
                i += 2
            i += 1

    if not contents[-1].isalpha():
        temp = contents[-1]
        contents = contents.strip(temp)
        contents = contents + " " + temp + " "

    content_lst = contents.split()
    succession = {".": [content_lst[0]]}

    for i in range(1,len(content_lst)):
        if content_lst[i - 1] in succession.keys() and content_lst[i] not in succession[content_lst[i-1]]:
            temp_lst = succession[content_lst[i-1]]
            temp_lst.append(content_lst[i])
            succession[content_lst[i-1]] = temp_lst
        elif content_lst[i-1] not in succession.keys():
            succession.update({f"{content_lst[i-1]}":[f"{content_lst[i]}"]})

    return succession



def getPosition(num, digit):

    # This function runs an iteration using the modulus/integer-division methodology. Going from right to left, it
    # searches for the digit in the number, and if found, records the location (named count in this function).  If not,
    # it returns false.

    count = 1
    while num > 0:
        rem = num % 10
        if rem == digit:
            return count
        num = num // 10
        count += 1

    return False



def hailstone(n):

    # This function checks whether the number is odd or even.  If even, the number is divided and placed in the list.
    # If odd, the number is multiplied by three and added to one, then appended to the list.  When the number reaches
    # 1 or lower, the function stops iterating and returns the list.

    lst = [n]


    while n > 1:
        if n % 2 == 0:
            lst.append(n//2)
            n = n // 2
        else:
            lst.append(3*n+1)
            n = 3 * n + 1


    return lst



def largeFactor(num):

    # The function determines the largest common factor by iterating upwards from 2, and recording the numbers that are
    # perfectly divisible with the original value.  After reaching the original value, the largest factor is returned.

    lcf = 1
    for i in range(2,num):
        if num % i == 0:
            lcf = i

    return lcf
