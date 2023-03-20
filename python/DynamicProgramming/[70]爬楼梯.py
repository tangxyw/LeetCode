from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i]表示爬上i阶台阶的不同方法数量, 故dp[n]为所求
        # 选择: 在位置i, 上一步是爬了1阶或爬了2阶
        # base case: dp[0] = 1, dp[1] = 1
        dp = [0] * (n+1)
        dp[0] = 1   # 0阶台阶, 1种方法(就是不爬)
        dp[1] = 1   # 1阶台阶, 1种方法
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]   # 上一步爬1阶方法数+上一步爬2阶方法数
        return dp[n]