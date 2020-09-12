def self_power_sum(limit=10):
    total = 0
    for i in range(1, limit + 1):
        total += i ** i
    return total


print(self_power_sum(1000))
