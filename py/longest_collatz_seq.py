memoized_collatz = {}


def collatz_count(n: int) -> int:
    init_n = n
    count = 0
    while n > 1:
        if n in memoized_collatz:
            count += memoized_collatz[n]
            memoized_collatz[init_n] = count
            return count
        else:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3*n+1
            count += 1
    memoized_collatz[init_n] = count
    return count


def problem_14():
    max_c = 0
    max_i = 0
    for i in range(1000000):
        cols = collatz_count(i)
        if cols > max_c:
            max_c = cols
            max_i = i
    return max_c, max_i


if __name__ == "__main__":
    print(problem_14())
