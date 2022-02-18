def recursive(row, col, row_target, col_target):
    if row == row_target and col == col_target:
        return 1

    if row >= row_target and col >= col_target:
        return 0

    if row >= row_target:
        return recursive(row, col+1, row_target, col_target)

    if col >= col_target:
        return recursive(row+1, col, row_target, col_target)
    
    left = recursive(row+1, col, row_target, col_target)
    down = recursive(row, col+1, row_target, col_target)
    
    return  left + down 

def solve(m,n):
    return recursive(0, 0, m-1, n-1)


print(solve(3,7))
