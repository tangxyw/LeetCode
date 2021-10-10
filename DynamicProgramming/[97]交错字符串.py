class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 题目没有说明, s3由s2开始交错也可以
        # 动态规划, 自底向上
        # 定义dp数组, n1 = len(s1), n2 = len(s2)
        # 状态: dp[i][j]定义为s1[:i]和s2[:j](也就是s1的前i个字符和s2的前j个字符)是否能交错组成s3[:i+j]
        #      故dp[n1][n2]为所求
        # 选择: 见代码注释
        # base case: dp[0][0] = 0
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False

        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 and j == 0:  # base case
                    dp[0][0] = True
                elif i == 0:  # 第1行, 为True的充要条件为前一个状态为True且s2对应的字符和s3相同
                    dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:  # 第1列, 逻辑同第1行
                    dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
                else:  # 其他位置的状态转移, 为True的充要条件为上一个位置或左边位置为True, 且和s3对应的字符相同
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                               (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[n1][n2]
