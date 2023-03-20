from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划
        # 定义dp数组, 形状和triangle相同, n = len(triangle)
        # 状态: dp[i][j]定义为从顶点triangle[0][0]走到triangle[i][j]的最短路径
        #      故min(dp[n-1])为所求
        # 选择: 见代码注释
        # base case: dp[0][0] = triangle[0][0]

        n = len(triangle)  # 三角形矩阵行数
        dp = []
        # dp形状和triangle相同
        for nums_per_row in range(1, n + 1):
            dp.append([0] * nums_per_row)

        for row_index in range(n):
            for j in range(row_index + 1):
                if row_index == 0:  # base case
                    dp[row_index][j] = triangle[row_index][j]
                elif j == 0:  # 每行的第一个位置
                    dp[row_index][j] = dp[row_index - 1][j] + triangle[row_index][j]
                elif j == row_index:  # 每行的最后一个位置
                    dp[row_index][j] = dp[row_index - 1][j - 1] + triangle[row_index][j]
                else:  # 每行中间位置
                    dp[row_index][j] = min(dp[row_index - 1][j], dp[row_index - 1][j - 1]) + triangle[row_index][j]

        return min(dp[n - 1])
