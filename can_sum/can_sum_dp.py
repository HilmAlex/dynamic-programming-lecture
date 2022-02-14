def recursive(target, numbers, memo):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in numbers:
        remainder = target-num

        if recursive(remainder, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


def solve(target, numbers):
    return recursive(target, numbers, {})


print(solve(7, [2, 3]))
print(solve(7, [5, 3, 4, 7]))
print(solve(300, [7, 14]))
