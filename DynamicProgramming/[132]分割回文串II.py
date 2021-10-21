class Solution:
    def minCut(self, s: str) -> int:
        # 动态规划
        # 定义dp数组, n = len(s), g[l][r]表示s[l:r+1]是否为回文子串
        # 状态: dp[i]表示s前i+1个字符组成的子串, 分割回文串的最小次数, 故dp[n-1]为所求
        # 选择: 见代码注释
        # base case: dp[0] = 0, 单个字符串就是回文字符串

        n = len(s)
        # 定义辅助矩阵g, g[l][r]表示s[l:r+1]是否为回文子串
        g = [[None for _ in range(n)] for _ in range(n)]
        # g也经由动态规划算出
        # 从矩阵底部向上, 从左到右遍历
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if l == r:  # 单个字符
                    g[l][r] = True
                elif s[l] == s[r]:  # 子串头尾字符相同
                    # 若子串长度大于等于2, g[l][r]由g[l+1][r-1]决定, 否则子串就为回文串
                    g[l][r] = g[l + 1][r - 1] if r - l > 1 else True
                else:  # 子串头尾字符不同, 不为回文串
                    g[l][r] = False

        dp = [float('inf')] * n
        dp[0] = 0  # base case
        for i in range(1, n):
            if g[0][i]:  # 子串本身就为回文串, 最小分割次数为0
                dp[i] = 0
            else:  # https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/
                for j in range(i):
                    if g[j + 1][i]:
                        dp[i] = min(dp[j] + 1, dp[i])

        return dp[n - 1]
