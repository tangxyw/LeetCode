from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i][j]为到达(i,j)的总路径数, 0<=i<=m-1, 0<=j<=n-1, 故dp[m-1][n-1]为所求
        # 选择: dp[i][j] = dp[i-1][j] + dp[i][j-1], 即走到上面格子的路径数+走到左边格子的路径数
        # base case: dp[0][j] = dp[i][0] = 1
        # 障碍处理: 有障碍的格子, 对应位置的dp[i][j] = 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        # 起点格子特殊处理
                        dp[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                    else:  # 第一行其他格子
                        dp[i][j] = dp[i][j - 1] if obstacleGrid[i][j] == 0 else 0
                elif j == 0:  # 第一列其他格子
                    dp[i][j] = dp[i - 1][j] if obstacleGrid[i][j] == 0 else 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if obstacleGrid[i][j] == 0 else 0

        return dp[m - 1][n - 1]
