class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 动态规划
        # 定义dp数组
        # 状态: dp[i][j]为s[i:j+1]的最长回文子序列长度, 故dp[0][n]为所求
        # 选择: 见注释
        # base case: dp[i][i] = 1, dp[i][j] = 0 (i < j)

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # 递归方向: 行从下至上, 列从左至右, 对角线下方全为0不变
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:  # 单个字符
                    dp[i][j] = 1
                else:  # 多个字符
                    if s[i] == s[j]:  # 两端字符相同
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:   # 两端字符不同, 所以两端字符不能成为最长回文子序列的两端
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
