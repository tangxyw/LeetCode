from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, len(prices) = n
        # 每天交易结束后只可能存在手里有一支股票或者没有股票的状态
        # 状态: dp[0][i]为第i天交易后, 手里没有股票的最大利润
        #       dp[1][i]为第i天交易后, 手里持有股票的最大利润
        #       故dp[0][n-1]为所求
        # 选择: 在第i天：
        #       dp[0][i]:
        #       1. 什么都不做, 即dp[0][i-1];
        #       2. 卖出股票, 即dp[1][i-1] + prices[i]
        #       两者取较大者
        #       dp[1][i]:
        #       1. 什么都不做, 即dp[1][i-1];
        #       2. 买入股票, 即dp[0][i-1] - prices[i]
        #       两者取较大者
        # base case: dp[0][0] = 0, dp[1][0] = -prices[0]
        n = len(prices)
        dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1],
                           dp[1][i-1] + prices[i])
            dp[1][i] = max(dp[1][i-1],
                           dp[0][i-1] - prices[i])

        return dp[0][n-1]
