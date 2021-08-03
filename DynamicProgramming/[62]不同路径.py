class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i][j]为到达(i,j)的总路径数, 0<=i<=m-1, 0<=j<=n-1, 故dp[m-1][n-1]为所求
        # 选择: dp[i][j] = dp[i-1][j] + dp[i][j-1], 即走到上面格子的路径数+走到左边格子的路径数
        # base case: dp[0] = nums[0]
        dp = [[0 for _ in range(n)] for _ in range(m)]  # 行数在外部, 列数在内部
        # 初始化base case和状态转移一起进行
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:  # base case
                    dp[i][j] = 1
                else:  # 状态转移
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]