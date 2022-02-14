tests = [
    [6,5,4,3,2,1,0,2],
    [1, 2, 2, 5, 2, 5, 2, 5, 5, 4, 4, 4, 4, 4, 2, 4, 0, 3, 3, 3, 4, 2, 4, 3, 2, 3, 5, 0, 3, 4, 2, 2, 1, 1, 3, 5, 2, 2, 4, 4, 1, 4, 1, 3, 5, 3, 1, 3, 1, 5,
        2, 0, 3, 5, 5, 2, 4, 0, 4, 3, 1, 4, 5, 0, 3, 4, 5, 2, 4, 5, 4, 4, 1, 5, 0, 4, 5, 0, 5, 2, 0, 5, 0, 3, 3, 4, 1, 5, 3, 4, 1, 1, 1, 2, 0, 5, 3, 5, 2, 1]
]


def recursive(idx, jumps, lastLeaf, memo):
    if idx == lastLeaf:
        return True

    if jumps[idx] == 0:
        return False

    for i in range(1, jumps[idx] + 1):
        if idx not in memo:
            memo[idx] = recursive(idx+i, jumps, lastLeaf, {})

        if memo[idx]:
            return True
    return False


def solve():
    return recursive(0, tests[1], len(tests[1]), {})


print(solve())
