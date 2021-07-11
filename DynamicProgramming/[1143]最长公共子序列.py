class Solution:
    """
    给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
    一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
    若这两个字符串没有公共子序列，则返回 0。

    示例 1:

    输入：text1 = "abcde", text2 = "ace"
    输出：3
    解释：最长公共子序列是 "ace"，它的长度为 3。

    """

    @staticmethod
    def longestCommonSubsequence_1(text1: str, text2: str) -> int:
        """
        递归解法
        :param text1: 字符串1
        :param text2: 字符串2
        :return: 最大公共子序列长度lcs
        """
        n = len(text1)
        m = len(text2)

        def dp(i, j):
            if i == -1 or j == -1: return 0
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(n - 1, m - 1)

    @staticmethod
    def longestCommonSubsequence_2(text1: str, text2: str) -> int:
        """
        带备忘录的递归解法
        :param text1: 字符串1
        :param text2: 字符串2
        :return: 最大公共子序列长度lcs
        """
        n = len(text1)
        m = len(text2)
        # 初始化备忘录, memo[i][j]表示text1[:i+1]与text2[:j+1]的lcs
        memo = [[-1 for j in range(m + 1)] for i in range(n + 1)]

        # memo[0][:] = [0 for i in range(m + 1)]
        # for j in range(1, n+1):
        #     memo[j][0] = 0

        def dp(i, j):
            # base case
            if i == 0 or j == 0: return 0
            # 在备忘录里查询到, 直接返回
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i - 1] == text2[j - 1]:
                memo[i][j] = dp(i - 1, j - 1) + 1
            else:
                memo[i][j] = max(dp(i - 1, j), dp(i, j - 1))
            return memo[i][j]

        return dp(n, m)

    @staticmethod
    def longestCommonSubsequence_3(text1: str, text2: str) -> int:
        """
        自底向上的动态规划解法
        :param text1: 字符串1
        :param text2: 字符串2
        :return: 最大公共子序列长度lcs
        """
        n = len(text1)
        m = len(text2)
        # 初始化dp table, 2维数组, 第1行第1列固定为0, dp[i][j]表示text1[:i+1]与text2[:j+1]的lcs, 最终dp[n][m]为所求
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        # 遍历dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 状态转移方程
                # 若text[:i]与text[:j]的最后一个字符相同, 则text[:i]与text[:j]的lcs为text[:i]与text[:j]各去掉最后一个字符的lcs加1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 最关键的部分, 若text[:i]与text[:j]的最后一个字符不同
                # 令s1 = {x1,x2,...,xn}, s2 = {y1,y2,...,ym}, z = {z1,z2,...,zk}, z为s1和s2的lcs, 未知
                # 当xn != ym, 分两种情况讨论:
                # (1) xn != zk: 则s1\{xn}与s2的lcs与s1与s2的lcs相同, 即都为z.
                # 反证法: 若则s1\{xn}与s2的lcs与s1与s2的lcs不同, 则必有lcs_s1\{xn}_s2 < lcs_s1_s2, 那么xn = zk, 矛盾
                # 同理可证:
                # (2) ym != zk: 则s1与s2\{ym}的lcs与s1与s2的lcs相同, 即都为z.
                # 故dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]


if __name__ == '__main__':
    # print(Solution.longestCommonSubsequence_1('bbach', 'abbch'))
    # print(Solution.longestCommonSubsequence_2('abcde', 'ace'))
    print(Solution.longestCommonSubsequence_3('abcde', 'ace'))
