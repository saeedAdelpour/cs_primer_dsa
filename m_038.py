def minimal_grid_path(grid, p=(0, 0), _sum=0, path=()):
    """Minimum path sum from the top-left cell to the bottom-right cell.

    From ``(0, 0)``, you may move only one step **down** or **right** until you
    reach ``(len(grid) - 1, len(grid[0]) - 1)``. Each move adds the value of
    the cell you step **into**; the starting cell is not added to the running
    sum.

    Args:
        grid: Rectangular matrix of numbers (list of rows, each a list).
        p: Current position ``(row, col)``. Intended for internal recursion;
            callers should rely on the default ``(0, 0)``.
        _sum: Accumulated sum for the path so far. For internal use; default ``0``.

    Returns:
        The smallest possible sum over all valid down/right paths to the
        bottom-right corner.
    """

    if p[0] == len(grid) - 1 and p[1] == len(grid[0]) - 1:
        return _sum, path

    ps = list(
        filter(
            lambda p: p[0] < len(grid) and p[1] < len(grid[0]),
            (
                (p[0] + 1, p[1]),  # button
                (p[0], p[1] + 1),  # right
            ),
        )
    )
    return min(
        minimal_grid_path(grid, _p, _sum + get_n(grid, _p), (*path, _p)) for _p in ps
    )


def get_n(grid, p):
    return grid[p[0]][p[1]]


if __name__ == "__main__":
    _sum, _path = minimal_grid_path(
        [
            [1, 2, 4, 3],
            [3, 4, 3, 2],
            [3, 6, 7, 3],
        ]
    )
    print(_sum, _path)
    assert _sum == 14

    _sum, _path = minimal_grid_path(
        [
            [1, 2, 2, 9],
            [3, 9, 3, 2],
            [3, 1, 9, 3],
        ]
    )
    print(_sum, _path)
    assert _sum == 12, _sum

    print("ok")
