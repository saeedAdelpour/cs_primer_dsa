"""
find the sum of all numbers that divisible by 3 or 5
"""


def way1_naive(n):
    # write a function that calculate the sum of numbers that divisible by 3 or 5
    # O(n)
    _sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            _sum += i
    return _sum


def way2_optimized(n):
    # O(1)
    def sum_divisible_by(n, target):
        p = target // n
        result = n * (p * (p + 1)) // 2
        print("n, target, p, result", [n, target, p, result])
        return result

    return (
        sum_divisible_by(3, n - 1)
        + sum_divisible_by(5, n - 1)
        - sum_divisible_by(15, n - 1)
    )


test_cases = [
    (10, 23),
    (1000, 233168),
    (1000000000, 233333333166666668),
]
for n, expected in test_cases:
    print(n, expected)
    print("way2_optimized")
    assert way2_optimized(n) == expected
    print("way1_naive")
    assert way1_naive(n) == expected
print("PASSED")
