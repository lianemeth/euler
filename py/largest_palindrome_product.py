def largest_palindrome_product():
    max_palindrome = 0
    for i in range(1000):
        for j in range(1000):
            n = i * j
            if n > max_palindrome and str(n)[::-1] == str(n):
                max_palindrome = n
    return max_palindrome


print(largest_palindrome_product())
