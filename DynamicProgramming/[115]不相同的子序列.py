def numDistinct(self, s: str, t: str) -> int:
    # 动态规划, 自底向上
    # 定义dp数组, n = len(s), m = len(t)
    # 状态: dp[i][j]定义为s[:i]的子序列t[:j]出现的次数(也就是s的前i个字符和t的前j个字符)
    #      故dp[n][m]为所求
    # 选择: 见代码注释
    # base case: dp[i][0] = 1, 空字符串为任意字符串的子序列
    #            dp[0][j] = 0, j = 1,2,...

    n = len(s)
    m = len(t)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if j == 0:  # base case
                dp[i][j] = 1
            elif i == 0:  # base case
                dp[i][j] = 0
            else:
                if s[i - 1] == t[j - 1]:  # s[:i]的最后一个字符和t[:j]最后一个字符相同
                    # 1. s[:i-1]中和t[:j-1]相同的子序列, 末尾都加上s[i-1], 这部分的个数为dp[i-1][j-1]
                    # 2. 不考虑s[:i]中的s[i-1], 用s[:i-1]的子序列来匹配t[:j], 这部分的个数为dp[i-1][j]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:  # s[:i]的最后一个字符和t[:j]最后一个字符不相同
                    # 只有上面的情况2
                    dp[i][j] = dp[i - 1][j]

    return dp[n][m]
