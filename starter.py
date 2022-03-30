def hailstone(n):
        yield n
        while n != 1:
            if n % 2 == 0:
                yield n / 2
                n /= 2
            else:
                yield n * 3 + 1
                n = n * 3 + 1