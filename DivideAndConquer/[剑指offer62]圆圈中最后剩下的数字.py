class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 约瑟夫圈问题
        # 动态规划
        # https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + m) % i

        return dp[n]
