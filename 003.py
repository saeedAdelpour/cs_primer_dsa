def find_binary_search(_list, item, list_with_index=None):
    if list_with_index == []:
        return -1

    elif list_with_index is not None:
        _list = list_with_index
    else:
        _list = [(i, x) for i, x in enumerate(_list)]
        _list = sorted(_list, key=lambda y: y[1])
    if not _list:
        return -1

    idx = len(_list) // 2
    value = _list[idx][1]
    if item == value:
        return _list[idx][0]
    elif item > value:
        return find_binary_search(None, item, _list[idx + 1 :])
    else:
        return find_binary_search(None, item, _list[:idx])


test_cases = (
    ([2, 1], 1, 1),
    ([4, 2, 7], 7, 2),
    ([3, 352, 44, 234, 23, 42, 42, 4], 23, 4),
    ([3, 352, 44, 234, 23, 42, 42, 4], 352, 1),
    ([-1, 3, 5, 2, 0], 2, 3),
    ## edge cases
    ([], 4, -1),
    ([3, 1, 2], 4, -1),
    ([3, 352, 44, 234, 23, 42, 42, 4], 100, -1),
    ([4, 23, 2, 3, 25, 26, 2, 242, 5, 2], 242, 7),
    # ([3, 0, 1, 2, 0], 0, 1),
)

for _list, item, expect in test_cases:
    idx = find_binary_search(_list, item)
    assert idx == expect, [_list, item, (expect, idx)]
print("ok")
