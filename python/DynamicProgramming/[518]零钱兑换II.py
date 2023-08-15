from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 动态规划
        # dp[i][j]表示使用前i个硬币凑出金额j的组合数
        # base case
        # dp[i][0] = 1 任取i
        # dp[0][j] = 0 任取j>0
        # 状态转移进代码

        n = len(coins)

        # 二维dp数组，第一行i=0表示不用任何硬币凑成0-amount的组合数，第一列j=0表示用前i个硬币凑成0的组合数(为1，即不用任何一个硬币)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:   # 状态转移
                    if j >= coins[i-1]:  # 金额j大于等于新增加的这个硬币的面额
                        # dp[i-1][j]为不用这个这个硬币的组合数, dp[i][j - coins[i-1]]表示用前i个硬币凑成金额j - coins[i-1]的组合数
                        dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                    else:   # 金额j小于新增加的这个硬币的面额
                        dp[i][j] = dp[i-1][j]

        return dp[n][amount]
