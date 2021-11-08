class Solution:
    def translateNum(self, num: int) -> int:
        # 动态规划, 自底向上
        # 定义dp数组, n = len(str(num))
        # 状态: dp[i]表示num前i+1个字符组成的子串的翻译方法数
        #       故dp[n-1]为所求
        # 选择: 见代码注释
        # base case: dp[0] = 1
        num = str(num)
        n = len(num)
        dp = [0] * n
        # base case
        dp[0] = 1
        for i in range(1, n):
            if "10" <= num[i - 1:i + 1] <= "25":  # 最后两个数字放在一起可以表示一个字母
                dp[i] = dp[i - 1] + dp[i - 2] if i - 2 >= 0 else dp[i - 1] + 1  # 此处要处理dp[1]的特殊逻辑
            else:  # 最后两个数字放在一起无法表示一个字母
                dp[i] = dp[i - 1]

        return dp[n - 1]
