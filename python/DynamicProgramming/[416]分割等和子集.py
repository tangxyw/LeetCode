from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # nums中所有元素都为正整数
        # X = Y成立 (X,Y都非空)
        # 当且仅当
        # X = S/2, 其中X + Y = S, S = sum(nums),
        # 问题转化为0-1背包问题, new_target = S/2
        # 动态规划, 自底向上
        # 定义dp数组, n = len(nums)
        # 状态: dp[i][j]为s是否能用nums[:i+1]凑成j(也就是nums的前i个值凑成j)
        #       故dp[n][new_target]为所求
        # 选择: 见代码注释
        # base case: dp[0][0] = True, (用[]凑0, 1种方法, 也就是[]), dp[0][j] = False, (用[]凑j, 没有方法)

        n = len(nums)
        S = sum(nums)
        if S % 2 == 1:
            return False

        new_target = S // 2

        dp = [[False for _ in range(new_target+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(new_target+1):
                # base case
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                else:   # [494]目标和 的简化版
                    if j < nums[i-1]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[n][new_target]