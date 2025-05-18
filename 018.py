"""
write a function that takes a unix path and convert it to a correct path
example:
    give "/etc/foo/../bar/baz.txt"
    return "/etc/bar/baz.txt"
"""


def to_path(unix_path):
    *dirs, file = unix_path.split("/")  # split is O(n)

    valid_dirs = []
    while dirs:
        _dir = dirs.pop()
        if _dir == "..":
            _ = dirs.pop()
        elif _dir == ".":
            pass
        else:
            valid_dirs.append(_dir)

    return "/".join([*(valid_dirs)[::-1], file])


if __name__ == "__main__":
    test_cases = (
        ("/etc/foo/../bar/baz.txt", "/etc/bar/baz.txt"),
        ("/etc/foo/./bar/baz.txt", "/etc/foo/bar/baz.txt"),
        ("/etc/x.txt", "/etc/x.txt"),
    )
    for unix_path, expect_output in test_cases:
        path = to_path(unix_path)
        assert path == expect_output, f"expect to be '{expect_output}', got '{path}'"
    print("ok")
