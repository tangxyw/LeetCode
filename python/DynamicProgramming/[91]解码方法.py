class Solution:
    def numDecodings(self, s: str) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, len(s) = n
        # 状态: dp[i]为s[:i+1]的不同解码结果数, 故dp[n-1]为所求
        # 选择: 见代码注释
        # base case: 见代码注释
        if s[0] == '0':  # 首数字为0, 无法解码
            return 0
        if len(s) == 1:  # 单数字, 只有1种解码方法
            return 1
        legalset = set([str(i) for i in range(1, 27)])  # 1-26才合法
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        if s[1] == '0':  # 第二个数字是0, 如果前两个数字合法, 则有1种解码方法, 不合法就没有解码方法
            dp[1] = 1 if s[:2] in legalset else 0
        else:  # 第二个数字合法, 如果前两个数字合法, 则有2种解码方法, 不合法就有1种解码方法
            dp[1] = 2 if s[:2] in legalset else 1

        # 状态转移
        for i in range(2, n):
            if s[i] == '0':  # 当前数字为0
                if s[i - 1:i + 1] in legalset:  # s[i-1:i+1]合法, 例如'10'
                    dp[i] = dp[i - 2]  # s[i-1:i+1]无法分离, 将s[i-1:i+1]加到dp[i-2]的每一种解码后面
                else:  # s[i-1:i+1]也不合法('00'), 无法解码
                    dp[i] = 0
            else:  # 当前数字合法
                if s[i - 1:i + 1] in legalset:  # s[i-1:i+1]也合法, 例如'11'
                    dp[i] = dp[i - 1] + dp[i - 2]  # 将s[i]加到dp[i-1]的每一种解码后面, 将s[i-1:i+1]加到dp[i-2]的每一种解码后面
                else:  # s[i-1:i+1]不合法, 例如'55'
                    dp[i] = dp[i - 1]  # 将s[i]加到dp[i-1]的每一种解码后面

        return dp[n - 1]