def hailstone(num):
    if num == 1:
        return [1]
    else:
        if num % 2 == 0:
            return [num] + hailstone(num//2)
        else:
            return [num] + hailstone(3*num+1)