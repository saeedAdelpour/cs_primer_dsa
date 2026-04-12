import enum
from rich import print


def choose(array, i=0, checking=[]):
    """
    this function takes a list of numbers and returns maximum sum of numbers
        that are not adjacent together
    for example:
        array = [4, 7, 8, 5, 3]
        then the numbers are: {4, 8, 3}, which sum = 15
    """
    checking_not_possible_idx = [
        _f for f in [(k - 1, k, k + 1) for k in checking] for _f in f
    ]

    possible_idx = [
        j
        for j in range(len(array))
        if j not in (i - 1, i, i + 1, *checking_not_possible_idx)
    ]
    if not possible_idx:
        idx = [i] + checking
        return sum([array[i] for i in idx]), idx
    res = []
    for _i in possible_idx:
        out = choose(array, i, [*checking, _i])

        if isinstance(out, list):
            for _o in out:
                res.append(_o)
        else:
            res.append(out)
    return res


if __name__ == "__main__":

    for test_idx, (array, expect_sum, expect_idx) in enumerate(
        [
            ([4, 7, 8, 5, 3], 15, [0, 2, 4]),
            ([3, 10, 1, 2, 20], 30, [1, 4]),
            ([3, 10, 8, 2, 20], 31, [0, 2, 4]),
        ]
    ):
        out = [j for i in range(len(array)) for j in choose(array, i)]
        out = sorted(out, key=lambda x: x[0], reverse=True)
        _sum, _idx = out[0]
        assert expect_sum == _sum, (test_idx, _sum)
        assert expect_idx == _idx, (test_idx, _idx)
    print("ok")
