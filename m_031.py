import ipdb
import sys
from itertools import product

import numpy as np
from rich import print


def find_next_positions(position, _map, route):
    max_x, max_y = _map.shape

    x = position[0]
    y = position[1]
    xs = [x, x + 1, x - 1]
    ys = [y, y + 1, y - 1]
    positions = list(product(xs, ys))[1:]

    out = []
    for p in positions:
        if 0 <= p[0] < max_x and 0 <= p[1] < max_y and p not in route:
            char = _map[p[0], p[1]]
            out.append((p, char))
    out.sort(key=lambda x: cost_map[x[1]])
    return out


cost_map = {
    ".": 5,
    "#": 10,
    " ": 1,
    "X": 0,
    "0": 0,
}


def find_position(_map, char):
    idx = np.where(_map == char)
    i = idx[0][0]
    j = idx[1][0]
    return (i, j)


def find_best_route(_map):
    origin = find_position(_map, "0")
    destination = find_position(_map, "X")

    todo_list = [
        (origin, ((origin,), 0)),
    ]
    checklist = set()
    final_routes = []
    max_todo_length = 0
    while todo_list:
        max_todo_length = max(max_todo_length, len(todo_list))
        position, (route, length) = todo_list.pop(0)
        next_positions = find_next_positions(position, _map, route)
        for next_position, char in next_positions:
            new_route = (*route, next_position)
            new_length = length + cost_map[char]

            if next_position == destination:
                final_routes.append((new_route, new_length))
                break

            found_better_in_todo_list = can_found_better_in_todo_list(
                next_position, todo_list, new_length
            )

            if next_position not in checklist and not found_better_in_todo_list:
                todo_list.append((next_position, (new_route, new_length)))
                todo_list = remove_not_better_from_todo_list(
                    next_position, new_length, todo_list
                )

        checklist.add(position)

    return final_routes, max_todo_length


def can_found_better_in_todo_list(position, todo_list, length):
    return any(
        _position
        for _position, (_route, _length) in todo_list
        if _position == position and _length <= length
    )


def remove_not_better_from_todo_list(position, length, todo_list):
    less_length_idx = [
        i
        for i, (_position, (_route, _length)) in enumerate(todo_list)
        if _position == position and _length > length
    ]
    same_length_idx = [
        i
        for i, (_position, (_route, _length)) in enumerate(todo_list)
        if _position == position and _length == length
    ]
    todo_list = [
        todo_list[i]
        for i in range(len(todo_list))
        if i not in less_length_idx + same_length_idx[1:]
    ]
    return todo_list


def draw_route(_map, route, path):
    __map = _map.copy()
    for p in route[1:-1]:
        __map[p[0], p[1]] = "*"
    out = "\n".join("".join(c for c in line) for line in __map)
    with open(path, "w") as fp:
        fp.write(out)


def debug():
    path = sys.argv[1]
    with open(path) as fp:
        _map = fp.readlines()
    _map = np.array([list(x[:-1]) for x in _map])
    final_routes, max_todo_length = find_best_route(_map)
    route, length = sorted(final_routes, key=lambda _r: _r[1])[0]
    print(route)
    print({"length": length, "max_todo_length": max_todo_length})


def test():
    path_length_pairs = (
        ("m_031_map_test_validity", 4, 7),
        ("m_031_map_test", 22, 24),
        ("m_031_map_test_1", 10, 30),
        ("m_031_map_test_2", 147, 137),
        ("m_031_map", 68, 69),
    )

    print("start test")
    for path, expect_length, expect_max_todo_length in path_length_pairs:
        print(f"test: {path}")
        with open(path) as fp:
            _map = fp.readlines()
        _map = np.array([list(x[:-1]) for x in _map])
        final_routes, max_todo_length = find_best_route(_map)
        route, length = sorted(final_routes, key=lambda _r: _r[1])[0]
        draw_route(_map, route, f"{path}_route")
        assert length == expect_length, f"{length} != {expect_length}, {path}"
        assert (
            max_todo_length == expect_max_todo_length
        ), f"{max_todo_length} != {expect_max_todo_length}, {path}"
    print("ok")


if __name__ == "__main__":
    # debug()
    test()
