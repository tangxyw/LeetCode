from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划, 考虑自底向上递推
        # 定义dp数组
        # 状态: dp[i]为打劫nums[:i]的最大收益, 故dp[n]为所求
        # 选择: 在位置i, 有打劫nums[i]和不打劫2种选择
        # base case: dp[n], dp[1] = 0, nums[0]

        n = len(nums)
        dp = [0] * (n + 1)

        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[n]
