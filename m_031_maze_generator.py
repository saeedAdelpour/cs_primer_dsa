import sys

from collections import defaultdict
from random import choices, randrange


h = sys.argv[1]
w = sys.argv[2]

TILES, WEIGHTS = "#. ", [3, 3, 4]
NUM_RUNS = 5


def top(M, i, j):
    out = defaultdict(lambda: 0)
    for ii in {max(0, i - 1), i, min(i + 1, len(M) - 1)}:
        for jj in {max(0, j - 1), j, min(j + 1, len(M[0]) - 1)}:
            out[M[ii][jj]] += 1

    return sorted(out.items(), key=lambda x: x[1], reverse=True)[0][0]


def make_map(H, W):
    # place mountains and bog
    M = ["".join(choices(list(TILES), weights=WEIGHTS, k=W)) for _ in range(H)]
    for _ in range(NUM_RUNS):
        M = [[top(M, i, j) for j, x in enumerate(row)] for i, row in enumerate(M)]
        # M = [top(M, i, j) for i, row in enumerate(M) for j, x in enumerate(row)]

    # place starting point
    while True:
        i, j = randrange(0, H // 2), randrange(0, W // 2)
        if M[i][j] in TILES:
            M[i][j] = "0"
            break

    # place goal
    while True:
        i, j = randrange(H // 2, H), randrange(W // 2, W)
        if M[i][j] in TILES:
            M[i][j] = "X"
            break

    return M


if __name__ == "__main__":
    m = make_map(int(h), int(w))
    print("\n".join("".join(c for c in line) for line in m))
