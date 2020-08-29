def even_fibo_sums(limit):
    sum_ = 0
    a, b = 1, 2
    while b <= limit:
        if b % 2 == 0:
            sum_ = sum_ + b
        aux = a
        a = b
        b = aux + b
    return sum_


print(even_fibo_sums(4000000))
