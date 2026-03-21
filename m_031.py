import sys
import operator
from itertools import product

import numpy as np
from rich import print

ops = (operator.add, operator.sub)
deltas = (1,)


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
        (origin, ([origin], 0)),
    ]
    checklist = set()
    final_routes = []
    while todo_list:
        position, (route, length) = todo_list.pop(0)
        next_positions = find_next_positions(position, _map, route)

        for next_position, char in next_positions:
            new_route = [*route, next_position]
            new_length = length + cost_map[char]

            if next_position == destination:
                final_routes.append((new_route, new_length))

            if next_position not in checklist:
                todo_list.append((next_position, (new_route, new_length)))

        checklist.add(position)

    return final_routes


if __name__ == "__main__":
    path = sys.argv[1]
    # path = "m_031_map_test"
    # path = "m_031_map_test_validity"
    with open(path) as fp:
        _map = fp.readlines()
    _map = np.array([list(x[:-1]) for x in _map])
    final_routes = find_best_route(_map)
    route, length = sorted(final_routes, key=lambda _r: _r[1])[0]
    print(route, length)
