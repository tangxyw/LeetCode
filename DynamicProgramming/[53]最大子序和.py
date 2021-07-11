from typing import List


class Solution:
    """
    给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

    """

    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        """
        动态规划解法
        :param nums: 整数数组
        :return: 连续子数组的最大和
        """
        # 定义dp table, 第i项代表以nums[i]为结尾的连续子数组的最大和
        dp = [0 for _ in range(len(nums))]
        # base case
        dp[0] = nums[0]
        # 存放最大值
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 状态转移方程
            res = max(dp[i], res)
        return res


if __name__ == "__main__":
    print(Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
