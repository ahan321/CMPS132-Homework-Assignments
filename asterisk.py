def asterisk(n):
    if n == 1:
        return "*"
    else:
        return "*" + asterisk(n-1)

print(asterisk(5))