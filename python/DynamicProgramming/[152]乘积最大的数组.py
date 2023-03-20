from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, len(nums) = n
        # 状态: dp[i][0], dp[i][1]分别为nums[:i+1]的连续子数组乘积的最小值和最大值, 故max(dp[:][1])为所求
        # 选择: 见代码注释
        # base case: dp[0][0], dp[0][1] = nums[0], nums[0]
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)] # n*2的数组
        dp[0][0], dp[0][1] = nums[0], nums[0]    # 0:min, 1:max
        res = dp[0][1]
        for i in range(1, n):
            if nums[i] > 0: # 当前数字大于0
                dp[i][1] = max(dp[i-1][1]*nums[i], nums[i]) # 连续子数组乘积的最大值取决于i-1时的最大值和当前数字
                dp[i][0] = min(dp[i-1][0]*nums[i], nums[i]) # 连续子数组乘积的最小值取决于i-1时的最小值和当前数字
            else:   # 当前数字小于等于0
                dp[i][1] = max(dp[i-1][0]*nums[i], nums[i]) # 连续子数组乘积的最大值取决于i-1时的最小值和当前数字
                dp[i][0] = min(dp[i-1][1]*nums[i], nums[i]) # 连续子数组乘积的最小值取决于i-1时的最大值和当前数字
            res = max(res, dp[i][1])    # 更新最大值
        return res