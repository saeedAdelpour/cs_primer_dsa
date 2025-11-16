import json
import operator

from rich import print


def find_next_positions_old(position, max_x, max_y, path):
    x = position[0]
    y = position[1]

    ops = (operator.add, operator.sub)

    next_positions = []
    for x_op in ops:
        for y_op in ops:
            for n1, n2 in ((2, 1), (1, 2)):
                _x = x_op(x, n1)
                _y = y_op(y, n2)
                if 0 <= _x < max_x and 0 <= _y < max_y:
                    p = (_x, _y)
                    if p not in path:
                        next_positions.append(p)
    return next_positions


DELTAS = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))


def find_next_positions(position, max_x, max_y, path):
    out = []
    for dx, dy in DELTAS:
        cx, cy = position[0] + dx, position[1] + dy
        if 0 <= cx < max_x and 0 <= cy < max_y and (cx, cy) not in path:
            out.append((cx, cy))
    return out


def knight_moves(max_x, max_y):
    start = (0, 0)
    todo_list = [(start, {start: None})]
    goal = max_x * max_y

    while todo_list:

        position, path = todo_list.pop()
        _max = len(path)
        print("max", _max)
        if len(path) == goal:
            return path

        next_positions = find_next_positions(position, max_x, max_y, path)
        next_positions.sort(
            key=lambda c: len(find_next_positions(c, max_x, max_y, path)), reverse=True
        )
        for next_position in next_positions:
            path_copy = path.copy()
            path_copy[next_position] = None
            todo_list.append((next_position, path_copy))

    return None

    raise Exception("can't found any routes")


if __name__ == "__main__":
    routes = knight_moves(7, 7)
    with open("routes.json", "w") as fp:
        json.dump(routes, fp, indent=2)
    # print(routes)

    # next_positions = find_next_nodes((4, 4), 8, 8)
    # print(next_positions)
