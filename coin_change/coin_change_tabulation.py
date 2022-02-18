# https://leetcode.com/problems/coin-change/

class Solution:     
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount - coin >= 0:
                    dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - coin])

        if dp[amount] == float('inf'):
          return -1
        
        return dp[amount]

solution = Solution()
print(solution.coinChange([1,3,6,5,4,7,10], 1200))