tests = [
    [1, 2, 2, 5, 2, 5, 2, 5, 5, 4, 0, 4, 4, 1, 5, 0, 4, 5, 0, 5, 2,
     4, 1, 5, 3, 4, 1, 1, 1, 2, 0, 0, 3, 5, 2, 1],
    [1, 2, 2, 5, 2, 5, 2, 5, 5, 4, 4, 4, 4, 4, 2, 4, 0, 3, 3, 3, 4, 2, 4, 3, 2, 3, 5, 0, 3, 4, 2, 2, 1, 1, 3, 5, 2, 2, 4, 4, 1, 4, 1, 3, 5, 3, 1, 3, 1,
     5, 2, 0, 3, 5, 5, 2, 4, 0, 4, 3, 1, 4, 5, 0, 3, 4, 5, 2, 4, 5, 4, 4, 1, 5, 0, 4, 5, 0, 5, 2, 0, 5, 0, 3, 3, 4, 1, 5, 3, 4, 1, 1, 1, 2, 0, 0, 3, 5, 2, 1]
]


def solve(jumps):
    dp = [False] * len(jumps)

    dp[len(jumps)-1] = True

    for i in range(len(jumps)-1, -1, -1):
        if True in dp[i: i+jumps[i]+1]:
            dp[i] = True

    return dp[0]


print(solve(tests[1]))
