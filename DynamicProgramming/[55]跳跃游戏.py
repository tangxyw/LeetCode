from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 动态规划, 自底向上
        # 定义dp数组, len(nums) = n
        # 状态: dp[i]为是否能够跳到index为i的结果, 故dp[n-1]为所求
        # 选择: 在index为i：
        #      j < i
        #      if dp[j] and j + nums[j] >= i:
        #            dp[i] = True
        # base case: dp[0] = True
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i-1, -1, -1):    # 遍历所有i前面的数j, 这里倒序遍历j, 可以缩短运行时间
                if dp[j] and j + nums[j] >= i:  # 若可以到达j 且 从j至少可以到达i
                    dp[i] = True
                    break   # 可以提前结束内层循环
        print(dp)
        return dp[n-1]