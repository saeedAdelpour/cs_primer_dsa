import operator

from rich import print


def find_next_positions(position, max_x, max_y, route):
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

                    if p not in route:
                        next_positions.append(p)

    return next_positions


def knight_moves(max_x, max_y):
    start = (0, 0)
    todo_list = [
        [
            start,
            [start],
        ],
    ]
    goal = max_x * max_y

    while todo_list:

        position, route = todo_list.pop()
        if len(route) == goal:
            return route

        next_positions = find_next_positions(position, max_x, max_y, route)
        next_positions.sort(
            key=lambda _p: len(find_next_positions(_p, max_x, max_y, route)),
            reverse=True,
        )

        for next_position in next_positions:
            todo_list.append([next_position, [*route, next_position]])

    return None


if __name__ == "__main__":
    routes = knight_moves(8, 8)
    print(routes)

    # next_positions = find_next_nodes((4, 4), 8, 8)
    # print(next_positions)
