from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, len(prices) = n
        # 状态: dp[i]为price[:i],即前i天的最大收益(i从0开始), 故dp[n-1]为所求
        # 选择: 在第i天：
        #       1. 什么都不做, 即dp[i-1];
        #       2. 卖出股票, 即price[i] - minprice, minprice为截至当前最小价格
        #       两者取较大者
        # base case: dp[0] = 0
        n = len(prices)
        dp = [0] * n
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1],    # 什么都不做
                         prices[i] - minprice)  # 卖出股票

        return dp[n-1]