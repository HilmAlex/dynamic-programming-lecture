
class Solution:
    def recursive(self, coins, current_coins, amount):
        if amount == 0:
            return current_coins

        if amount < 0:
            return float('inf')

        min_coins = float('inf')

        for coin in coins:
            min_coins = min(min_coins, self.recursive(
                coins, current_coins + 1, amount - coin))

        return min_coins

    def coinChange(self, coins, amount: int) -> int:
        answer = self.recursive(coins, 0, amount)

        if answer == float('inf'):
            return -1

        return answer



solution = Solution()
print(solution.coinChange([1,3,6,5,4,7,10], 1200))