import math

class Solution:
    def numSquares(self, n: int) -> int:
        # 等价于零钱兑换问题, 即完全背包问题
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i]为凑成正整数i的完全平方数的最少数量, 故dp[n]为所求
        # 选择: dp[i]取决于所有的dp[i-num]+1的最小值
        # base case: dp[0] = 0, 不需要任何数就能凑出0

        max_num = int(math.sqrt(n)) # n的平方根向下取整
        squares = [x*x for x in range(1, max_num+1)]    # 保证所需要的完全平方数, 不会超过n
        dp = [float('inf')] * (n+1) # 注意这里是n+1
        dp[0] = 0
        for i in range(1, n+1):
            for num in squares:
                if i >= num:    # 只有i>=num时, 才能用num来凑i
                    dp[i] = min(dp[i], dp[i-num]+1)
        return dp[n]