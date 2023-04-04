class Solution:
    def numDecodings(self, s: str) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, len(s) = n
        # s前要加空格, 方便迭代
        # 状态: dp[i]为s[:i]的不同解码结果数, 故dp[n]为所求
        # 选择: 见代码注释
        # base case: 见代码注释
        n = len(s)
        s = ' ' + s
        dp = [0] * (n + 1)
        dp[0] = 1   # 空格处的解码方法数为1
        for i in range(1, n + 1):
            a = ord(s[i]) - ord('0')    # s[i]对应的一位数字
            b = (ord(s[i - 1]) - ord('0')) * 10 + ord(s[i]) - ord('0')  # s[i-1]和s[i]对应的两位数字
            if 1 <= a <= 9:    # 当前一位数字a合法
                dp[i] += dp[i - 1]
            if 10 <= b <= 26:   # 当前两位数字b合法
                dp[i] += dp[i - 2]  # 注意i=1时, b肯定是负数, 所以不会执行这里, 不用担心i-2为负
        return dp[n]
