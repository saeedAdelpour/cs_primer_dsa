"""
exp(a, n) = a * a * a * a ... * a (n times)
"""


def exp(a, n):
    """
    O(n)
    """
    print("exp")
    if n == 1:
        return a
    return a * exp(a, n - 1)


def exp_o_log_n(a, n):
    """
    made
    O(log n)
    to achieve this, we should divide and conquer

    3 ^ 8 = 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3
            ------------- * -------------
    3 ^ 9 = 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3
            ------------- * ------------- * 3
    """
    print("exp_o_log_n")

    if n == 1:
        return a

    half = exp_o_log_n(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * a


if __name__ == "__main__":

    test_cases = (
        (2, 3, 8),
        (2, 4, 16),
        (3, 3, 27),
        (4, 7, 16384),
        (4, 8, 65536),
        (3, 8, 6561),
    )

    for a, n, expect_output in test_cases:
        print("test: a, n, expect_output", a, n, expect_output)

        output = exp(a, n)
        assert output == expect_output, [output, expect_output]
        output_o1 = exp_o_log_n(a, n)
        assert output_o1 == expect_output, [output_o1, expect_output]

    print("ok")
