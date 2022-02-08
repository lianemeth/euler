import math


def count_divisor(n):
    i = 1
    count = 0
    while i <= math.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                count += 1
            else:
                count += 2
        i += 1
    return count


def problem_12():
    i = 1
    tri = 0
    div = 0
    while div < 500:
        tri = tri + i
        div = count_divisor(tri)
        print(tri, div)
        i += 1
    return tri


if __name__ == "__main__":
    print(problem_12())
