from rich import print


def choose_iterative(xs):
    pp, p = 0, 0
    for x in xs:
        pp, p = p, max(x + pp, p)
    return p


def choose_opt(xs):
    memo = {}

    def __choose_opt(ys):
        try:
            return memo[len(ys)]
        except KeyError:
            pass
        if len(ys) in memo:
            return memo[len(ys)]
        if len(ys) == 1:
            return ys[0]
        if len(ys) == 0:
            return 0
        res = max(ys[0] + __choose_opt(ys[2:]), __choose_opt(ys[1:]))
        memo[len(ys)] = res
        return res

    x = __choose_opt(xs)
    return x


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

        _sum_opt = choose_opt(array)
        assert _sum_opt == expect_sum, (_sum_opt, expect_sum)

        _sum_iterative = choose_iterative(array)
        assert _sum_iterative == expect_sum, (_sum_iterative, expect_sum)
    print("ok")
