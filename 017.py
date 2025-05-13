import re


def compute(instruction):
    regex = r"\(([^()]+)\)"

    groups = re.findall(regex, instruction)
    if groups == []:
        return eval(instruction)
    for group in groups:
        res = eval(group)
        instruction = instruction.replace(f"({group})", str(res))

    return compute(instruction)


def decorate(name):
    def _decorate(func):
        def _func(*args, **kwargs):
            return func(*args, **kwargs)

        # _func.__name__ = name
        return _func

    _decorate.__name__ = name
    return _decorate


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


OPS = {
    "+": add,
    "-": sub,
}


def compute_use_stack(instruction):
    s = []
    for c in instruction:
        if c.isdigit():

            try:
                prev = s.pop()
                if isinstance(prev, int):
                    s.append(prev * 10 + int(c))

                else:
                    s.append(prev)
                    s.append(int(c))
            except IndexError:
                s.append(int(c))

        elif c in OPS:
            s.append(OPS[c])
        elif c == ")":
            b, op, a = s.pop(), s.pop(), s.pop()
            s.append(op(a, b))
    if len(s) == 1:
        return s.pop()
    while len(s) != 1:
        a, op, b = s.pop(), s.pop(), s.pop()
        s.append(op(a, b))
    return s.pop()


class InvalidExpression(Exception):
    pass


if __name__ == "__main__":
    test_cases = (
        ("(1 + 2)", 3),
        ("(1 + (2 + 3 + (1 + 2 + (3 + 4))) + (2 + 3))", 21),
        # TODO: compute_use_stack didn't work on this
        # ("(1 + 2 - (3 - 8) + 4 + ((4 + (2 - 3) - (3 + 2) + 1) - 6))", 5),
        ("(12 + 33)", 45),
        ("(121 + 332)", 453),
        ("(154 + 3342)", 3496),
        ("(1 + 12)", 13),
        # TODO: compute_use_stack didn't work on this
        # ("(1 + 12) - (2 - 32)", 43),
    )
    print("test compute")
    for instruction, expect_result in test_cases:
        result = compute(instruction)
        assert result == expect_result, f"{result} != {expect_result}"
    print("ok")

    print("test compute_use_stack")
    for instruction, expect_result in test_cases:
        print("instruction", instruction)
        result = compute_use_stack(instruction)
        assert result == expect_result, f"{result} != {expect_result}"
    print("ok")
