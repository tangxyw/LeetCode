from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 动态规划
        # 定义dp数组
        # 状态: dp[i][j]表示以nums1索引为i-1为结尾 和 以nums2索引为j-1为结尾 的最大公共子数组长度
        # 转移方程: 见代码, 注意与[1143]的不同
        # base case: dp[i][0] = dp[0][j] = 0
        m = len(nums1)
        n = len(nums2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])

        return res
