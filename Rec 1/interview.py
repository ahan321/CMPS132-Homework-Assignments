def solution(A):
    binary = []
    for i in A:
        value = ""
        # Converting values to binary
        while i > 0:
            if i % 2 == 1:
                value += "1"
            else:
                value += "0"
        binary.append(value)

    # determining number of digits to use
    max_len = len(binary[0])
    for i in binary:
        if len(i) > max_len:
            max_len = len(i)

    # standardizing the number of digits

    for i in range(len(binary)):
        if len(binary[i]) < max_len:
            difference = max_len - len(binary[i])
            for j in range(difference):
                binary[i] = "0" + binary[i]

    # check if all digits can be ANDed
    value = ""
    for i in range(len(max_len)):
        count = 0
        for j in range(len(binary)):
            if int(binary[j][i]) != 1:
                value += 0
            else:
                count += "1"
                break
        if count == len(binary):
            value += "1"




