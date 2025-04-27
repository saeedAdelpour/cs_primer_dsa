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


if __name__ == "__main__":
    test_cases = (
        ("1 + (2 + 3 + (1 + 2 + (3 + 4))) + (2 + 3)", 21),
        ("1 + 2", 3),
        ("1 + 2 - (3 - 8) + 4 + ((4 + (2 - 3) - (3 + 2) + 1) - 6)", 5),
    )
    for instruction, expect_result in test_cases:
        result = compute(instruction)
        assert result == expect_result, f"{result} != {expect_result}"
    print("ok")
