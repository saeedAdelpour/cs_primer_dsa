# objective:            implement merge sort
# final objective 1:    try to write this function in space complexity of O(n)
# final objective 2:    try to write this function in space complexity of *O(1)*


def merge_sort(_list):
    if not _list:
        return []

    if len(_list) == 1 and isinstance(_list[0], list):
        return _list[0]

    if not all(isinstance(x, list) for x in _list):
        groups = [[x] for x in _list]
    else:
        groups = _list

    result = []
    for first_index in range(0, len(groups), 2):
        last_index = first_index + 1
        g1 = groups[first_index]
        try:
            g2 = groups[last_index]
        except IndexError:
            result.append(g1)
            continue

        g = []
        while g1 or g2:

            if g1:
                n1 = g1[0]
            else:
                n1 = None

            if g2:
                n2 = g2[0]
            else:
                n2 = None

            if n1 is None:
                g.append(n2)
                g2 = g2[1:]
            elif n2 is None:
                g.append(n1)
                g1 = g1[1:]
            elif n1 > n2:
                g.append(n2)
                g2 = g2[1:]
            else:
                g.append(n1)
                g1 = g1[1:]

        result.append(g)
    return merge_sort(result)


def merge_sort_optimized(_list):
    working = _list.copy()

    def merge(left, mid, right):

        il = left
        ir = mid

        for i in range(left, right):

            if (ir != right and working[il] > working[ir]) or il == mid:
                _list[i] = working[ir]
                ir += 1
            else:
                _list[i] = working[il]
                il += 1

        for i in range(left, right):
            working[i] = _list[i]

    def sort(left, right):
        if right - left <= 1:
            return

        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    sort(0, len(_list))
    return _list


if __name__ == "__main__":
    test_cases = (
        (
            [4, 8, 2, 1, 3, 9, 7],
            [1, 2, 3, 4, 7, 8, 9],
        ),
        (
            [10, 9, 8, 7, 6],
            [6, 7, 8, 9, 10],
        ),
        (
            [10, 9, 8, 7],
            [7, 8, 9, 10],
        ),
        (
            [8, 4, 5, 1, 2, 9, 0],
            [0, 1, 2, 4, 5, 8, 9],
        ),
        (
            [1],
            [1],
        ),
        (
            [1, 2],
            [1, 2],
        ),
        (
            [2, 1],
            [1, 2],
        ),
        (
            [1, 2, 3],
            [1, 2, 3],
        ),
        (
            [],
            [],
        ),
    )
    for _list, expect_output in test_cases:
        print("_list, expect_output", _list, expect_output)
        _sorted = merge_sort(_list)
        assert (
            _sorted == expect_output
        ), f"_sorted={_sorted}, expect_output={expect_output}"
    print("ok")

    for _list, expect_output in test_cases:
        print("_list, expect_output", _list, expect_output)
        _sorted = merge_sort_optimized(_list)
        assert (
            _sorted == expect_output
        ), f"_sorted={_sorted}, expect_output={expect_output}"

    print("ok")
