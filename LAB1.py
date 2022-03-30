# Lab #1
# Due Date: 09/03/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


def joinList(n):
    # This function starts by checking whether n is positive, and then constructs an ascending
    # and descending list based on n. Both lists are then extended to complete_lst, which is
    # then returned to finish the function.  If n is negative, None is returned.
    
    if n > 0:
        asct_lst = list(range(1,n+1,1))
        desc_lst = list(range(n,0,-1))
        complete_lst = []
        complete_lst.extend(asct_lst)
        complete_lst.extend(desc_lst)
    else:
        return None
    
    return complete_lst



def isValid(txt):
    # This function starts by checking whether variable txt is a string, and returning none
    # if so.  It then checks that the length of txt is 26 characters, returning false if it
    # isn't satisfied.  All characters are then made lowercase. The function then iterates 
    # through the ASCII codes of lowercase characters in order to check if each one is
    # present.  If satisfied, the function returns true.

    if type(txt) != str:
        return None
    
    if len(txt) != 26:
        return False

    txt = txt.lower()

    for i in range(ord("a"), ord("z")+1):
        if chr(i) not in txt:
            return False

    return True





def removePunctuation(aString):
    # The function starts by iterating through the characters in aString looking for characters
    # that are not alphabets. When found, the function counts the occurences of this character, 
    # places them in a dictionary, before replacing the characters with spaces. This repeats until
    # the for loop reaches the end of the string.  The space character is then popped from the dictionary
    # as it was counted as well, and both values are returned to the user.

    freq = {}
    for i in range(len(aString)):
        if not aString[i].isalpha():
            freq[aString[i]] = aString.count(aString[i])

            aString = aString.replace(aString[i]," ")

    freq.pop(" ")
    return aString, freq