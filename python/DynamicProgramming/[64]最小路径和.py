from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i][j]为到达(i,j)的最小路径数, 0<=i<=m-1, 0<=j<=n-1, 故dp[m-1][n-1]为所求
        # 选择: dp[i][j] = min(dp[i-1][j] + dp[i][j-1]) + grid[i][j], 即取到上面格子的最小路径数和走到左边格子的最小路径数的最小值, 再加上(i,j)格子的步数
        # base case: dp[0][0] = grid[0][0]
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:  # 起点格子特殊处理
                        dp[i][j] = grid[i][j]
                    else:  # 第一行
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:  # 第一列
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]
