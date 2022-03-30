# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    count = 0
    pointer1 = 1
    pointer2 = 2
    # counting from left to right
    for i in range(len(S) - 3):
        arr1 = S[:pointer1 + 1]
        arr2 = S[pointer1 + 1:pointer2 + 1]
        arr3 = S[pointer1 + 1:]

        if "a" in arr1 and "a" in arr2 and "a" in arr3:
            count += 1
        pointer2 += 1