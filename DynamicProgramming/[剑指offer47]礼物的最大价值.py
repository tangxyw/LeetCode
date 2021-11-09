from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i][j]为到达(i,j)能拿到的最大价值, 0<=i<=m-1, 0<=j<=n-1, 故dp[m-1][n-1]为所求
        # 选择: dp[i][j] = max(dp[i-1][j] + dp[i][j-1]) + grid[i][j], 即比较走到上面格子的最大价值和走到左边格子的最大价值, 取较大者, 再加上(i,j)格子的价值
        # base case: 见注释

        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:  # 起点格子
                    dp[i][j] = grid[i][j]
                elif i == 0:  # 第一行
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:  # 第一列
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]
