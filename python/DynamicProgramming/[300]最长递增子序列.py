from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i]结尾为nums[i]的最长递增子序列, 故max(dp[:])为所求
        # 选择: 见代码注释
        # base case: dp[0] = 1, 第1个数字本身构成子序列
        n = len(nums)
        dp = [1] * n
        res = dp[0]
        for i in range(1, n):
            for j in range(i):  # 遍历所有nums[:i]
                if nums[i] > nums[j]:   # 当nums[i] > nums[j]时, 意味着i可以放在以nums[j]为结尾的子序列后面形成新的递增子序列
                    dp[i] = max(dp[i], dp[j]+1) # 在其中选最长的
            res = max(res, dp[i])   # 在dp数组中选择最大的

        return res
