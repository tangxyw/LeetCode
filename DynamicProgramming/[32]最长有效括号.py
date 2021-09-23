class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # https://leetcode-cn.com/problems/longest-valid-parentheses/solution/shou-hua-tu-jie-zhan-de-xiang-xi-si-lu-by-hyj8/
        # 动态规划, 自底向上
        # 定义dp数组
        # 状态: dp[i]表示以s[i]为结尾的合法子串的最长长度, 故max(dp)为所求
        # 选择: 见代码注释和reference
        # base case: dp[0] = 0
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            elif s[i] == ')':
                if s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2  # s[i-1]和s[i]组成了有效括号长度为2
                    else:
                        dp[i] = 2
                elif s[i - 1] == ')':
                    # 从i往前跨过dp[i-1]个字符, 考虑s[i-dp[i-1]-1]
                    if i - dp[i - 1] - 1 < 0:  # 下标不合法
                        dp[i] = 0
                    elif i - dp[i - 1] - 1 >= 0:
                        if s[i - dp[i - 1] - 1] == '(':
                            if i - dp[i - 1] - 2 >= 0:
                                dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
                            else:
                                dp[i] = dp[i - 1] + 2
                        elif s[i - dp[i - 1] - 1] == ')':
                            dp[i] = 0

        return max(dp)
