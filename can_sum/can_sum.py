def recursive(target, numbers):
    if target == 0:
        return True

    if target < 0:
        return False

    for num in numbers:
        remainder = target-num

        if recursive(remainder, numbers):
            return True

    return False


def solve(target, numbers):
    return recursive(target, numbers)


print(solve(7, [2, 3]))
print(solve(7, [5, 3, 4, 7]))
print(solve(300, [7, 14]))
