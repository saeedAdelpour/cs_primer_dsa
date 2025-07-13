def quick_sort(_list):
    if len(_list) == 0:
        return []

    pivot = _list[0]
    left = []
    right = []
    for a in _list[1:]:
        if a < pivot:
            left.append(a)
        else:
            right.append(a)

    return [*quick_sort(left), pivot, *quick_sort(right)]


def quick_sort_inplace_course(nums):
    """
    [4, 1, 3, 2, 5]
    p = 4

    [1, 4, 3, 2, 5]
    [1, 3, 4, 2, 5]


    [4, 5, 1, 3, 2]



    """

    def sort(lo, hi):
        if hi <= lo:
            return

        m = lo
        for i in range(lo + 1, hi + 1):
            if nums[i] < nums[lo]:
                m += 1
                nums[i], nums[m] = nums[m], nums[i]
        nums[lo], nums[m] = nums[m], nums[lo]

        sort(lo, m - 1)
        sort(m + 1, hi)

    sort(0, len(nums) - 1)


if __name__ == "__main__":

    for _list, expect_output in (
        (
            [4, 1, 3, 2, 5],
            [1, 2, 3, 4, 5],
        ),
        (
            [4, 5, 1, 3, 2],
            [1, 2, 3, 4, 5],
        ),
        (
            [5, 8, 1, 3, 9, 11, 12],
            [1, 3, 5, 8, 9, 11, 12],
        ),
        (
            [8, 6, 7, 4],
            [4, 6, 7, 8],
        ),
        (
            [3, 1, 3, 4, 4, 1, 2, 7, 2],
            [1, 1, 2, 2, 3, 3, 4, 4, 7],
        ),
        (
            [1],
            [1],
        ),
        (
            [],
            [],
        ),
    ):
        output = quick_sort(_list)
        assert output == expect_output, [output, expect_output]

        quick_sort_inplace_course(_list)
        assert _list == expect_output, [_list, expect_output]
    print("ok")
