import math


def perfect_square(n, count=0):
    if n == 0:
        return count
    max_near = int(math.sqrt(n))
    max_near = max_near**2
    return perfect_square(n - max_near, count + 1)


if __name__ == "__main__":
    for n, nums, count in (
        (7, (4, 1, 1, 1), 4),
        (14, (9, 4, 1), 3),
        (23, (16, 4, 1, 1, 1), 5),
        # (23, (9, 9, 4, 1), 4),
    ):
        ps = perfect_square(n)
        assert ps == count, (ps, count)
    print("ok")
