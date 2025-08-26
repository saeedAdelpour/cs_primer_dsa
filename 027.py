import sys

from rich import print


class _Process:
    pid: int
    children: "list[_Process] | None"
    args: str | None

    def __init__(self, pid, children, args):
        self.pid = pid
        self.children = children
        self.args = args

    def __repr__(self):
        return f"pid: {self.pid}>, args: {self.args}"


def to_info(line):
    pid, ppid, *args = [x for x in line.strip().split(" ") if x]
    return int(pid), int(ppid), args
    return int(pid), int(ppid), "args"


def print_pstree(root, level=0):
    print("*" * level, root)
    for ps in root.children:
        print_pstree(ps, level + 1)


def main():
    ps = {}
    # with open("ps") as f:
    #     lines = list(iter(f))[1:]

    lines = list(sys.stdin.readlines())[1:]
    for line in lines:
        pid, ppid, *args = to_info(line)
        if ppid in ps:
            parent = ps[ppid]
        else:
            parent = _Process(ppid, [], None)
            ps[ppid] = parent

        if pid in ps:
            child = ps[pid]
        else:
            child = _Process(pid, [], "args")
            ps[pid] = child

        parent.children.append(child)

    print_pstree(ps[0])


if __name__ == "__main__":
    main()
