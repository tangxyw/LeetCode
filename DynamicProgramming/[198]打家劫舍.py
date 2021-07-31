from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划, 考虑自底向上递推
        # 定义dp数组
        # 状态: dp[i]为打劫nums[i:]的最大收益, 故dp[0]为所求
        # 选择: 在位置i, 有打劫nums[i]和不打劫2种选择
        # base case: dp[n], dp[n+1] = 0, 0
        n = len(nums)
        dp = [0] * (n + 2)  # 隐含了base case
        for i in range(n - 1, -1, -1):  # 倒序遍历索引
            dp[i] = max(nums[i] + dp[i + 2],  # 打劫nums[i]
                        dp[i + 1])  # 不打劫nums[i]
        return dp[0]
