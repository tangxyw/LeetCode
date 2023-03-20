from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # nums中所有元素都为正整数
        # target = X - Y成立 (X为nums中前面添加+的元素集合, Y为nums中前面添加-的元素集合)
        # 当且仅当
        # X = (target + S)/2, 其中S = X + Y = sum(nums)
        # 问题转化为0-1背包问题, new_target = (target + S)/2
        # 动态规划, 自底向上
        # 定义dp数组, n = len(nums)
        # 状态: dp[i][j]为用nums[:i+1]凑成j的方法数(也就是nums的前i个值凑成j)
        #       故dp[n][new_target]为所求
        # 选择: 见代码注释
        # base case: dp[0][0] = 1, (用[]凑0, 1种方法, 也就是[]), dp[0][j] = 0, (用[]凑j, 没有方法)

        S = sum(nums)
        if target > S or target < -S or (target + S) % 2 == 1:    # target绝对值大于S 或者 new_target不为整数
            return 0

        n = len(nums)
        new_target = (target + S) // 2

        dp = [[0 for _ in range(new_target+1)] for _ in range(n+1)]

        # 遍历方向: 逐行
        for i in range(n+1):
            for j in range(new_target+1):
                # base case
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                # 选择, 选或者不选nums[i-1] (i-1为nums第i个元素的索引)
                else:
                    if j < nums[i-1]:   # j-nums[i-1]<0, nums[i-1]比要凑的值都大, 这时无法选择nums[i-1]
                        dp[i][j] = dp[i-1][j]
                    else:   # j-nums[i-1]>=0, 用nums[:i+1]凑成j的方法数由两部分求和而来:
                            # 1. 不选num[i-1], 对应dp[i-1][j]
                            # 2. 选nums[i-1], 对应dp[i-1][j-nums[i-1]]
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]

        return dp[n][new_target]