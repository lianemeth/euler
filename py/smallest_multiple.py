def smallest_multiple():
    n = 1
    divisible = False
    while not divisible:
        n += 1
        for i in range(1, 11):
            inner_div = True
            if n % i != 0:
                inner_div = False
                break
        divisible = inner_div
    return n

print(smallest_multiple())
