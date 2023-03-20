class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 由于add和del对称, replace自对称, 所以最短编辑距离是对称的
        # 动态规划, 自底向上
        # 定义dp数组, m = len(word1), n = len(word2)
        # 状态: dp[i][j]为word1[:i+1]和word2[j+1](也就是word1的前i个字符和word2的前j个字符)的最短编辑距离
        #       故dp[m][n]为所求
        # 选择: 见代码注释
        # base case: dp[0][j] = j, dp[i][0] = i, 索引为0表示相应的字符串为空

        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                # 初始化base case
                if i == 0 or j == 0:
                    dp[i][j] = i if j == 0 else j
                else:  # 注意i-1和j-1分别是word1的第i个字符和word2的第j个字符的索引
                    if word1[i - 1] == word2[j - 1]:  # word1的第i个字符和word2的第j个字符相同
                        dp[i][j] = dp[i - 1][j - 1]
                    else:  # word1的第i个字符和word2的第j个字符不同, 取下列三个状态的最小值再加1
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[m][n]