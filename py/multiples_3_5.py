def sum_multi_3_and_5(n):
    sum_ = 0
    for i in range(n):
        if i % 3 == 0:
            sum_ += i
        elif i % 5 == 0:
            sum_ += i
    return sum_

print(sum_multi_3_and_5(1000))
