import math
from rich import print


def perfect_square(n):
    memo = {}

    def __perfect_square(n, count=0, nums=tuple()):
        if n in memo:
            return memo[n]

        if n == 0:
            return count, nums

        max_near = int(math.sqrt(n))
        squares = [i**2 for i in range(max_near, 1, -1)]
        if not squares:
            return __perfect_square(n - 1, count + 1, (*nums, 1))

        res = min(
            (__perfect_square(n - sq, count + 1, (*nums, sq)) for sq in squares),
            key=lambda x: x[0],
        )
        memo[n] = res
        return res

    x = __perfect_square(n)
    return x


if __name__ == "__main__":
    for n, nums, count in (
        (7, (4, 1, 1, 1), 4),
        (14, (9, 4, 1), 3),
        (23, (9, 9, 4, 1), 4),
        (35, (25, 9, 1), 3),
        (54, (49, 4, 1), 3),
        (4343, (4225, 100, 9, 9), 4),
        (30001, (29929, 36, 36), 3),
        (40101, (40000, 100, 1), 3),
    ):
        _count, _nums = perfect_square(n)
        assert _count == count, _count
        assert (_nums) == (nums), _nums
    print("ok")
