from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态规划
        # 定义dp数组
        # 状态: dp[i][j]表示以matrix[i][j]为右下顶点的正方形的最大边长
        # 转移方程: 见代码
        # base case: 见代码
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:    # base case
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1 if matrix[i][j] == '1' else 0
                res = max(res, dp[i][j])

        return res * res