from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, len(nums) = n
        # 状态: dp[i]为以i为结尾的所有子数组的最大和, 故max(dp[i])为所求
        # 选择: 在第i天：
        #       1. 取i-1的结果加上nums[i], 即dp[i-1]+nums[i];
        #       2. 只取nums[i]
        # base case: dp[0] = nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i],
                        nums[i])
            res = max(res, dp[i])

        return res
