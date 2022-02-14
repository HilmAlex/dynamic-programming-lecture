def recursive(row, col, paths, row_target, col_target):
    if row == row_target and col == col_target:
        return 1

    if row >= len(paths) and col >= len(paths[0]):
        return 0

    if row >= len(paths):
        return recursive(row, col+1, paths, row_target, col_target)

    if col >= len(paths[0]):
        return recursive(row+1, col, paths, row_target, col_target)

    return recursive(row+1, col, paths, row_target, col_target) + recursive(row, col+1, paths, row_target, col_target)


test = [
    [0, 1, 2, 4, 5, 6, 7],
    [0, 1, 2, 4, 5, 6, 7], 
    [0, 1, 2, 4, 5, 6, 7]
]


def solve():
    return recursive(0, 0, test, 2, 6)


print(solve())
